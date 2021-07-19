import random
# #Total Number of Games
# # Games = 10
# try: 
#     Games = int(input("How many games do you have in total (default = 10):"))
# except:
#     print('\nPlease input an integer! Default value is used\n')
#     print('--------------------------------------------------')
#     Games = 10

# # Games per AMI
# try:
#     GamesPerAMI = int(input('How many games do you wish to put inside 1 ami (default = 3):'))
# except:
#     print('\nPlease input an integer! Default value is used\n')
#     print('--------------------------------------------------')
#     GamesPerAMI = 3    

# #Total number of ami requred
# AMI = Games/GamesPerAMI
# if not AMI.is_integer():
#     AMI = Games//GamesPerAMI + 1


AMI_list = {
    "Counter-Strike:_Global_Offensive" : 379569,
    "Dota_2" : 304536,
    "PLAYERUNKNOWN'S_BATTLEGROUNDS" : 183353,
    "Apex_Legends" : 122892,
    "Grand_Theft_Auto_V" : 92447,
    "Team_Fortress_2" : 72341,
    "Rust" : 70773,
    "Warframe" : 56371,
    "Dead_by_Daylight" : 45615,
    "ARK:_Survival_Evolved" : 43722,
    "Tom_Clancy's_Rainbow_Six_Siege" : 42475,
    "Destiny_2" : 41539,
    "FINAL_FANTASY_XIV_Online" : 34756,
    "Sid_Meier's_Civilization_VI" : 30873,
    "Football_Manager_2021" : 28214,
    "Terraria" : 27359,
    "PAYDAY_2" : 25458,
    "Total_War:_WARHAMMER_II" : 24722,
    "Stardew_Valley" : 24711,
    "Unturned" : 24159,
    "Rocket_League" : 20610,
    "Garry's_Mod" : 19342,
    "War_Thunder" : 18374,
    "Black_Desert" : 18341,
    "VRChat" : 17970,
    "Hearts_of_Iron_IV" : 17272,
    "Monster_Hunter_Stories_2:_Wings_of_Ruin": 17208,
    "Left_4_Dead_2" : 16873,
    "Don't_Starve_Together" : 16680,
    "Monster_Hunter:_World" : 16505,
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
                    temp_game = random.choices(list(AMI_list.keys()), weights=(20.46,16.42,9.88,6.62,4.98,3.9,3.82,3.04,2.46,2.36,2.29,2.24,1.87,1.66,1.52,1.47,1.37,1.33,1.33,1.3,1.11,1.04,0.99,0.99,0.97,0.93,0.93,0.91,0.9,0.89), k=1)
                    newData.write(f"{new[0]} {new[1]} {new[2]} {temp_game[0]}\n")
                elif (new[1] == 'action'):
                    newData.write(f"{new[0]} {new[1]} {new[2]} GameID\n")
                else:
                    newData.write(f"{new[0]} {new[1]} {new[2]} null\n")
    print('newDataSet.txt created!')
except:
    print('Error encountered, please report to CloudDevGaming')


# print(f)