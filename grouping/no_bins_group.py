import csv
import binpacking

def write_to_file(grplist):
    filename = "group.csv"
    f = open(filename, "w", encoding="utf-8")
    headers = "Bin No, Space\n"
    f.write(headers)

retlist = {}
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

f.close()

groups = binpacking.to_constant_bin_number(retlist, 33)

rpg = [list(group.keys()) for group in groups]
realValues = [sum(group.values()) for group in groups]

filename = "group.csv"
f = open(filename, "w", encoding="utf-8")
headers = "Bin No, Games, Total Space\n"
f.write(headers)
for i in range(len(groups)):
    bin_no = str(i+1)
    games = ", ".join(rpg[i])
    tspace = "{:.2f}".format(realValues[i])
    f.write( bin_no + "," + games + "," + tspace + "\n")

f.close()