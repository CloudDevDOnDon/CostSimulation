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
    "Dota 2": 10,
    "Counter Strike: Global Offensive" : 10,
    "Valorant" : 8,
    "League of Legends": 10,
    "Monster Hunter World": 8,
    "MapleStory" : 8,
    "Rainbow Six: Siege" : 8,
    "OverCooked! 2" : 8,
    "Fall Guys! Ultimate Knockout": 8,
    "Fortnite": 9,
    "The Crew 2": 4,
    "Assasin's Creed: Valhalla": 5,
    "The Division 2": 3,
    "Watch Dogs Legion": 2,
    "Phantasy Star Online 2": 5,
    "For Honor": 1,
    "Ghost Recon Breakpoint" : 1,
    "World of Warcraft": 6,
    "Final Fantasy XIV": 6,
    "MineCraft": 5,
    "Left 4 Dead 2": 5,
    "Forza Horizon 4": 5,
    "Player Unknowns Battleground": 7,
    "Call of Duty Black Ops: Modern Warfare": 5,
    "Destiny 2": 3,
    "Runescape 3" : 5,
    "Old School Runescape" : 6,
    "Halo: The Master Chief Collection": 4,
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