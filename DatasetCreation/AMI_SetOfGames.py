import random
import pandas as pd


game = pd.read_csv("pop_128_group.csv")

AMI_list = (game.iloc[:,0].tolist())
Weighted = (game.iloc[:,2].tolist())


try:
    with open('newDataSet.txt', 'w') as newData:
        with open('dataset.txt', 'r') as data:
            for line in data:
                new = line.strip('\n').split(' ')
                if (new[1] == 'start'):
                    temp_game = random.choices(AMI_list, weights=Weighted, k=1)
                    newData.write(f"{new[0]} {new[1]} {new[2]} {temp_game[0]}\n")
                elif (new[1] == 'action'):
                    newData.write(f"{new[0]} {new[1]} {new[2]} GameID\n")
                else:
                    newData.write(f"{new[0]} {new[1]} {new[2]} null\n")
    print('newDataSet.txt created!')
except Exception as e:
    #print('Error encountered, please report to CloudDevGaming')
    print(e)


# print(f)