import random
#Total Number of Games
# Games = 10
try: 
    Games = int(input("How many games do you have in total (default = 10):"))
except:
    print('\nPlease input an integer! Default value is used\n')
    print('--------------------------------------------------')
    Games = 10

# Games per AMI
try:
    GamesPerAMI = int(input('How many games do you wish to put inside 1 ami (default = 3)'))
except:
    print('\nPlease input an integer! Default value is used\n')
    print('--------------------------------------------------')
    GamesPerAMI = 3    

#Total number of ami requred
AMI = Games/GamesPerAMI
if not AMI.is_integer():
    AMI = Games//GamesPerAMI + 1

# print(AMI)

# Variable processing
try:
    with open('newDataSet.txt', 'w') as newData:
        with open('dataset.txt', 'r') as data:
            for line in data:
                new = line.strip('\n').split(' ')
                if (new[1] == 'start'):
                    newData.write(f"{new[0]} {new[1]} {new[2]} {random.randrange(1,AMI)}\n")
                elif (new[1] == 'action'):
                    newData.write(f"{new[0]} {new[1]} {new[2]} GameID\n")
                else:
                    newData.write(f"{new[0]} {new[1]} {new[2]} null\n")
    print('newDataSet.txt created!')
except:
    print('Error encountered, please report to CloudDevGaming')


# print(f)