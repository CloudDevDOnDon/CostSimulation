"""

INTIAL PREP 

1. Importing required packages
2. Loading excel files
3. Reading 2 different styles
    1. Input Variable: Inputs that should be changed depending on the condition of the experiment
    2. Fixed Variable: Variables that are fixed by AWS. (Only change if any of the pricing changes)
4. Loading all the fixed variable for easy access

"""
## Import
import pandas as pd

## Loading the excel file
xls = pd.ExcelFile('Input for Cost Calculation.xlsx')

## Reading different sheets
inVarSheet = pd.read_excel(xls, 'Input Variable', index_col= 0, skiprows=[0])
fixVarSheet = pd.read_excel(xls, 'Fixed Variable', index_col= 0)
# print(inVarSheet)
# print(fixVarSheet)

## Prep all the fixed variable
ec2Cost = fixVarSheet.loc["EC2 Instance Cost","Rate"]
ebsRates = fixVarSheet.loc["Amazon EBS Rates","Rate"]
snapshotRates = fixVarSheet.loc["Amazon Snapshot Rates","Rate"]
dataTransferIn = fixVarSheet.loc["Data Transfer (In)", "Rate"]
dataTrasferOut = fixVarSheet.loc["Data Transfer (Out)", "Rate"].split(',')
lambdaRequestRates = fixVarSheet.loc["AWS Lambda request", "Rate"]
lambdaComputeRates = fixVarSheet.loc["AWS Lambda compute time ", "Rate"]


"""
 CALCULATING EC2 COST

1. Loading required variables for EC2 Calculation
2. Calculations:
    AWS EC2 Instance: 
        
        Total instance hour x EC2 hourly rates = Total EC2 hourly cost
    
    Amazon EBS (Volume): 
        
        Total instance hour / 730 (hours in a month) = Instance Months
        Instance Volume x Instance Month x EBS Volume rates = Total EBS volume cost 
"""
## Variables
optimizedInstanceHours = inVarSheet.loc["Instance Hours","Optimized"]
nonOptimizedInstanceHours = inVarSheet.loc["Instance Hours","Not Optimized"]

ebsVolumeSize = inVarSheet.loc["Storage Volume","Not Optimized"]

##Calculation
optimizedHoursCost = optimizedInstanceHours * ec2Cost  ###
nonOptimizedHoursCost = nonOptimizedInstanceHours * ec2Cost  ###

optimizedInstanceMonth = optimizedInstanceHours / 730
nonOptimizedInstanceMonth = nonOptimizedInstanceHours / 730

optimizedVolumeCost = optimizedInstanceMonth * ebsVolumeSize * ebsRates  ###
nonOptimizedVolumeCost = nonOptimizedInstanceMonth *ebsVolumeSize * ebsRates  ###

"""
CALCULATING AMI COST

1. Loading required variables for EC2 Calculation
2. Calculations:
    Amazon EBS (Snapshot): 

        Number of AMIs x Average snapshot utilisation x Snapshot rate = Total snapshot cost
    
    Data Transfer In:

        Free -> no calculation required

    Data Transfer Out:

        Average hourly data transfer rate x Total session = Total Data Transfer
        Total Data Transfer x DT rates = Total DT cost
 
"""
## Variables
noOfSnpshot = inVarSheet.loc["Number of snapshot","Not Optimized"]
averageSnpshotSize = ebsVolumeSize * inVarSheet.loc["Percentage of Storage Used","Not Optimized"]
dataTransfer = inVarSheet.loc["Data Transfer","Not Optimized"]
gameSession = inVarSheet.loc["Game Session","Not Optimized"]

## Calculation
snpShotCost = noOfSnpshot * averageSnpshotSize * snapshotRates

totalDataTransfer = dataTransfer * gameSession ##Fixed variable 
if totalDataTransfer > 10000:
     dataTransferCost = 9999*float(dataTrasferOut[0]) + (totalDataTransfer - 9999) * float(dataTrasferOut[1]) 
else:
    dataTransferCost = totalDataTransfer*float(dataTrasferOut[0])

"""
CALCULATING LAMBDA & CLOUDWATCH COST

1. Loading required variables for EC2 Calculation
2. Calculations:
    AWS Lambda request: 
        
        Under 1M request:
            Lambda request rates
        
        Over 1M request:
            Lambda request rates x Total Request / 1M = Total Lambda request cost
    
    AWS Lambda Compute Time:
        Total request x Compute Time Rates x lambda Execute Time = Total Lambda Execute Cost
        
"""
## Variable
lambdaRequest = inVarSheet.loc["Number of Request","Optimized"]
lambdaExecuteTime = inVarSheet.loc["Average Time to execute request","Optimized"]

## Calculation
if lambdaRequest < 1000000:
    lambdaRequestCost = lambdaRequestRates
else:
    lambdaRequestCost = lambdaRequest//1000000 * lambdaRequestRates

lambdaExecuteCost = lambdaRequest * lambdaExecuteTime//1000 * lambdaComputeRates


"""
PREPARE FOR EXPORTING


"""
totalNonOptCost = nonOptimizedHoursCost + nonOptimizedVolumeCost + snpShotCost + dataTransferCost 
totalOptCost = optimizedHoursCost + optimizedVolumeCost + snpShotCost + dataTransferCost + lambdaRequestCost + lambdaExecuteCost
costSavings = (totalNonOptCost - totalOptCost)/totalNonOptCost * 100

## Preparing the rows for exporting
row1 = f"All Games split into AMI ({ebsVolumeSize}GB)"
row2 = f"Service,Rate,Not Optimized,Optimized"
row3 = f"Instances"
row4 = f"AWS EC2 Instance (g4dn.xlarge),${ec2Cost},{nonOptimizedInstanceHours}hrs x ${ec2Cost} = ${nonOptimizedHoursCost},{optimizedInstanceHours}hrs x ${ec2Cost} = ${optimizedHoursCost}"
row5 = f"Amazon EBS (Volume),${ebsRates},{nonOptimizedInstanceHours} / 730 = {round(nonOptimizedInstanceMonth,2)} instance months\n{ebsVolumeSize}GB x {round(nonOptimizedInstanceMonth,2)} instance months x ${ebsRates} = ${round(nonOptimizedVolumeCost,2)},{optimizedInstanceHours} / 730 = {round(optimizedInstanceMonth,2)} instance months\n{ebsVolumeSize}GB x {round(optimizedInstanceMonth,3)} instance months x ${ebsRates} = ${round(optimizedVolumeCost,2)}"
row6 = f"AMI"
row7 = f"Amazon EBS (Snapshot),{snapshotRates} per GB-month of data stored,{noOfSnpshot} Snapshot x {averageSnpshotSize} GB x ${snapshotRates} = ${round(snpShotCost,2)}"
row8 = f"Data Transfer (In),Free,$0"
row9 = f"Data Transfer (Out),${dataTrasferOut[0]} per GB-month for next 9.999TB/month\n${dataTrasferOut[1]}per GB for next 40TB/month,${round(dataTransferCost,2)}"
row10 = f"Lambda & Cloudwatch"
row11 = f"AWS Lambda request,${lambdaRequestRates} per 1M request,$0(Not Used),${lambdaRequestCost}(under 1M request)"
row12 = f"AWS Lamdba compute time,${lambdaComputeRates} per 1000ms,$0(Not Used),{round(lambdaRequest)} x {lambdaExecuteTime}ms x ${lambdaComputeRates} = ${round(lambdaExecuteCost,2)}"
row13 = f"Amazon CloudWatch Events,Free,$0(Not Used),$0"
row14 = f",Total,${round(totalNonOptCost,2)},${round(totalOptCost,2)} ({round(costSavings,1)}% savings)"

## Exporting
tableData = [row1.split(','),row2.split(','),row3.split(','),row4.split(','),row5.split(','),row6.split(','),row7.split(','),row8.split(','),row9.split(','),row10.split(','),row11.split(','),row12.split(','),row13.split(','),row14.split(',')]
df = pd.DataFrame(tableData)
df.to_csv('toBeLatex.csv')