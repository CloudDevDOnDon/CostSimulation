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
    "Dota_2": 10,
    "Counter_Strike:_Global_Offensive" : 10,
    "Valorant" : 8,
    "League_of_Legends": 10,
    "Monster_Hunter_World": 8,
    "MapleStory" : 8,
    "Rainbow_Six:_Siege" : 8,
    "OverCooked!_2" : 8,
    "Fall_Guys!_Ultimate_Knockout": 8,
    "Fortnite": 9,
    "The_Crew_2": 4,
    "Assasin's_Creed:_Valhalla": 5,
    "The_Division_2": 3,
    "Watch_Dogs_Legion": 2,
    "Phantasy_Star_Online_2": 5,
    "For_Honor": 1,
    "Ghost_Recon_Breakpoint" : 1,
    "World_of_Warcraft": 6,
    "Final_Fantasy_XIV": 6,
    "MineCraft": 5,
    "Left_4_Dead_2": 5,
    "Forza_Horizon+_4": 5,
    "Player_Unknowns_Battleground": 7,
    "Call_of_Duty_Black_Ops:_Modern_Warfare": 5,
    "Destiny_2": 3,
    "Runescape_3" : 5,
    "Old_School_Runescape" : 6,
    "Halo:_The_Master_Chief_Collection": 4,
    "Tera" : 4,
    "WarFrame": 6
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
                    temp_game = random.choices(list(AMI_list.keys()), weights=(80,80,80,80,80,80,80,80,80,80,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20), k=1)
                    newData.write(f"{new[0]} {new[1]} {new[2]} {temp_game[0]}\n")
                elif (new[1] == 'action'):
                    newData.write(f"{new[0]} {new[1]} {new[2]} GameID\n")
                else:
                    newData.write(f"{new[0]} {new[1]} {new[2]} null\n")
    print('newDataSet.txt created!')
except:
    print('Error encountered, please report to CloudDevGaming')


# print(f)