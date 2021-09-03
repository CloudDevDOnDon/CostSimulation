import csv
import binpacking

retlist = {}
retpop = {}
sumer = 0
with open('games.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        game_name = row[0]
        spstr = row[4].split(": ")
        if("GB" in spstr[1]):
            space = float(spstr[1].split("GB")[0].strip())
        elif("MB" in spstr[1]):
            space = float(spstr[1].split("MB")[0].strip()) / 1000
        retlist[game_name] = space
        retpop[game_name] = row[1]
        sumer += int(row[1])

f.close()

groups = binpacking.to_constant_bin_number(retlist, 33)

rpg = [list(group.keys()) for group in groups]
realValues = [sum(group.values()) for group in groups]

filename = "group.csv"
f = open(filename, "w", encoding="utf-8")
headers = "Bin No, Games, Weighted Probability, Total Space\n"
f.write(headers)
for i in range(len(groups)):
    bin_no = str(i+1)
    games = "; ".join(rpg[i])
    tspace = "{:.2f}".format(realValues[i])
    temp_players = 0
    with open('games.csv', newline='') as fifi:
        reader = csv.reader(fifi)
        next(reader, None)
        for row in reader:
            game_name = row[0]
            if(game_name in rpg[i]):
                temp_players += int(retpop[game_name])
        weighted_prob = temp_players / int(sumer)
    fifi.close()
    f.write( bin_no + "," + games + "," + str(weighted_prob) + "," + tspace + "\n")

f.close()