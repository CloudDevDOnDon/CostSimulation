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


# AMI_list = {
#     "Counter-Strike: Global Offensive" : 379569,
#     "Dota 2" : 304536,
#     "PLAYERUNKNOWN'S BATTLEGROUNDS" : 183353,
#     "Apex Legends" : 122892,
#     "Grand Theft Auto V" : 92447,
#     "Team Fortress 2" : 72341,
#     "Rust" : 70773,
#     "Warframe" : 56371,
#     "Dead by Daylight" : 45615,
#     "ARK: Survival Evolved" : 43722,
#     "Tom Clancy's Rainbow Six Siege" : 42475,
#     "Destiny 2" : 41539,
#     "FINAL FANTASY XIV Online" : 34756,
#     "Sid Meier's Civilization VI" : 30873,
#     "Football Manager 2021" : 28214,
#     "Terraria" : 27359,
#     "PAYDAY 2" : 25458,
#     "Total War: WARHAMMER II" : 24722,
#     "Stardew Valley" : 24711,
#     "Unturned" : 24159,
#     "Rocket League" : 20610,
#     "Garry's Mod" : 19342,
#     "War Thunder" : 18374,
#     "Black Desert" : 18341,
#     "VRChat" : 17970,
#     "Hearts of Iron IV" : 17272,
#     "Monster Hunter Stories 2: Wings of Ruin" : 17208,
#     "Left 4 Dead 2" : 16873,
#     "Don't Starve Together" : 16680,
#     "Monster Hunter: World" : 16505,
# }

AMI_list = {
    "eSports" : ["Dota_2", "Counter_Strike: Global_Offensive", "Apex_Legends", "PLAYERUNKNOWN'S_BATTLEGROUNDS", "Tom Clancy's_Rainbow Six Siege"],
    "MMORPG" : ["Final Fantasy XIV", "Destiny 2", "Black Desert", "VRChat", ],
    "Survival" : ["ARK: Survival Evolved" , "Unturned", "Don't Starve Together"],
    "Co-Op": ["Grand Theft Auto V", "Rust", "Warframe" , "Dead by Daylight"],
    "FPS" : ["Team Fortress 2", "PAYDAY 2", "Left 4 Dead 2"],
    "RPG/Strategy" : ["Sid Meier's Civilization VI", "Hearts of Iron IV", "Monster Hunter Stories 2: Wings of Ruin", "Monster Hunter: World"],
    "Others" : ["Football Manager 2021", "Terraria", "Stardew Valley", "Rocket League", "Garry's Mod", "War Thunder" ]
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
                    temp_game = random.choices(list(AMI_list.keys()), weights=(55.68,6.07,4.56,14.3,6.18,4.41,7.47), k=1)
                    newData.write(f"{new[0]} {new[1]} {new[2]} {temp_game[0]}\n")
                elif (new[1] == 'action'):
                    newData.write(f"{new[0]} {new[1]} {new[2]} GameID\n")
                else:
                    newData.write(f"{new[0]} {new[1]} {new[2]} null\n")
    print('newDataSet.txt created!')
except:
    print('Error encountered, please report to CloudDevGaming')


# print(f)