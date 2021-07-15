# CostSimulation

## Description
Programs used by the team to generate data for the report.

### Folders Explanation
- Dataset Used: Dataset used to simulate in our report
- Dataset Creation:
    - AMI_allGames: attach ami (30 in total, each containing 1 game) to each session at a weighted chance randomly
    - AMI_SetOFGamesRandom: attach ami (6 in total, each containing 5 games) to each session at a weighted chance randomly
    - Randomiser: Allow user to create their own dataset randomly. Note: this is less accurate compared to using the WOW_session 
- DatasetSimulator: Run simulation based on the number of ami in total

# HOW TO USE
## Required Packages
1. Pandas -> <code>pip install pandas</code>

## General
1. In your chosen command-line/ terminal.
2. Navigate to the project folder

### To create Dataset
1. type <code>python DatasetCreation\Randomiser.py</code> 
2. type <code>python "DatasetCreation\AMI Random.py"</code>

### To test data
#### If all instances runs a single AMI
1. type <code>python DatasetSimulator\Simulator_SingleAMI\DatasetSimulator.py</code> 
2. type <code>python DatasetSimulator\Simulator_SingleAMI\DatasetSimulatorOptimized.py</code> 

#### If different instance has multiple AMI
1. type <code>python DatasetSimulator\Simulator_MultipleAMI\DatasetSimulator.py</code> 
2. type <code>python DatasetSimulator\Simulator_MultipleAMI\DatasetSimulatorOptimized.py</code> 