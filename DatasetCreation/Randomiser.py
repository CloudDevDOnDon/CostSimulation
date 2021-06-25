import random
# Variables

# Number of Users
Users = 30

# Number of records
Records = 10000

#Time
timestamp = 0
increment = 60 #in seconds

#Total Number of Games
Games = 10

# Games per AMI
GamePerAMI = 3

#Total number of ami requred
AMI = 10/3
if not AMI.is_integer():
    AMI = 10//3 + 1


# Variable processing
# Status Checks
user_status = {}
for user in range (1,Users+1):
    user_status[user] = 'start'

# Fuff 
Blank = Users
Userslist = Users + Blank

f = open('dataset.txt', 'w')
f.write('id action timestamp AMIID\n')
x = 0


while x < Records:
    timestamp += increment
    ID = random.randrange(1,Userslist)
    if ID < Users:
        x += 1
        if user_status[ID] == 'start':
            f.write(f"{ID} {user_status[ID]} {timestamp} {random.randrange(1,AMI)}\n")
            user_status[ID] = 'end'
        else:
            f.write(f"{ID} {user_status[ID]} {timestamp} null\n")
            user_status[ID] = 'start'


for i in user_status:
    timestamp += increment
    if user_status[i] == 'end':
        f.write(f"{ID} {user_status[ID]} {timestamp} null\n")

# print(f)