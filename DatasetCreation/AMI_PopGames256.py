import random

AMI_list = {
    "Bin_1" : ["Counter-Strike:_Global_Offensive", "Dota_2", "PLAYERUNKNOWN'S_BATTLEGROUNDS","Apex_Legends", "Grand_Theft_Auto_V"],
    "Bin_2" : ["Tom_Clancy's_Rainbow_Six_Siege", "Destiny_2", "FINAL_FANTASY_XIV_Online"],
    "Bin_3" : ["PAYDAY_2", "Total_War:_WARHAMMER_II", "Stardew_Valley", "Unturned"],
    "Bin_4": ["Monster_Hunter_Stories_2:_Wings_of_Ruin", "Left_4_Dead_2", "Don't_Starve_Together", "Monster_Hunter:_World"],
    "Bin_5": ["Team_Fortress_2", "Rust", "Warframe", "Dead_By_Daylight", "ARK:Survival_Evolved"],
    "Bin_6": ["Sid_Meier's_Civilization_VI", "Football_Manager_2021", "Terraria"],
    "Bin_7": [ "Rocket_League", "Garry's_Mod", "War_Thunder", "Black_Desert", "VRChat", "Hearts_of_Iron_IV"],
}

# print(AMI)
# print(random.choices(list(AMI_list.keys()), weights=(80,80,80,80,80,80,80,80,80,80,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20), k=1))
# Variable processing
try:
    with open('newDataSet.txt', 'w') as newData:
        with open('dataset.txt', 'r') as data:
            for line in data:
                new = line.strip('\n').split(' ')
                if (new[1] == 'start'):
                    temp_game = random.choices(list(AMI_list.keys()), weights=(53.39,15.74,7.11,5.78,5.70,7.74,4.56), k=1)
                    newData.write(f"{new[0]} {new[1]} {new[2]} {temp_game[0]}\n")
                elif (new[1] == 'action'):
                    newData.write(f"{new[0]} {new[1]} {new[2]} GameID\n")
                else:
                    newData.write(f"{new[0]} {new[1]} {new[2]} null\n")
    print('newDataSet.txt created!')
except:
    print('Error encountered, please report to CloudDevGaming')


# print(f)