import random
# Variables

# Number of Users
Users = 10

# Number of records
Records = 50

#Time
timestamp = 0
increment = 1000 #in seconds


# Variable processing
# Status Checks
user_status = {}
for user in range (1,Users+1):
    user_status[user] = 'start'

# Fuff/ to simulate chances (example: 20 users + 20 blanks = 50 %
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
            f.write(f"{ID} {user_status[ID]} {timestamp}\n")
            user_status[ID] = 'end'
        else:
            f.write(f"{ID} {user_status[ID]} {timestamp}\n")
            user_status[ID] = 'start'


for i in user_status:
    timestamp += increment
    if user_status[i] == 'end':
        f.write(f"{i} {user_status[i]} {timestamp}\n")

# print(f)