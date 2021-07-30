# CostSimulation

## Description
Programs used by the team to generate data for the report.

### Folders Explanation
- Dataset Used: Dataset used to simulate in our report
- Dataset Creation:
    - AMI_allGames: attach ami (30 in total, each containing 1 game) to each session at a weighted chance randomly
    - AMI_SetOFGames: attach ami (7 in total, sorted by genre) to each session at an equal chance randomly
    - AMI_PopGames256 / 512: attach ami (7 / 4 in total, sorted by popularity) to each session at a weighted chance randomly
    - Randomiser: Allow user to create their own dataset randomly. Note: this is less accurate compared to using the WOW_session 
- DatasetSimulator: Run simulation based on the number of ami in total
- GraphCreation: python file for create graphs in pdf format for overleaf report
- steamChart: Contain information on the games we choose for the simulation

# HOW TO USE
## Required Packages
1. Pandas -> <code>pip install pandas</code>
2. matplotlib -> <code>pip install matplotlib</code>

## General
1. In your chosen command-line/ terminal.
2. Navigate to the project folder

### To create Dataset
1. type <code>python DatasetCreation\Randomiser.py</code> 

### To assign AMI 
1. type <code>python "DatasetCreation\AMI_allGames.py"</code>
2. type <code>python "DatasetCreation\AMI_PopGames256.py"</code>
3. type <code>python "DatasetCreation\AMI_PopGames512.py"</code>
4. type <code>python "DatasetCreation\AMI_SetOfGames.py"</code>

### To test data
#### If all instances runs a single AMI
1. type <code>python DatasetSimulator\Simulator_SingleAMI\DatasetSimulator.py</code> 
2. type <code>python DatasetSimulator\Simulator_SingleAMI\DatasetSimulatorOptimized.py</code> 

#### If different instance has multiple AMI
1. type <code>python DatasetSimulator\Simulator_MultipleAMI\DatasetSimulator.py</code> 
2. type <code>python DatasetSimulator\Simulator_MultipleAMI\DatasetSimulatorOptimized.py</code> 

### To create graph
1. Place csv file into the GraphCreation folder
2. Run either the python or ipynb file