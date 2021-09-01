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

count = 0
ami_space = 256 * 0.7
gamelist = {
    "bin_1" : [],
    }
gamespace = {
    "bin_1" : [],
}
bin_spaces = {
    "bin_1" : ami_space
}

binz = 2
while count < len(retlist):
    for key,value in dict(retlist).items():
        bin = 1
        added = False
        while len(bin_spaces) > bin - 1:
            bin_name = "bin_" + str(bin)
            if value < bin_spaces[bin_name] and not added:
                gamelist[bin_name].append(key)
                gamespace[bin_name].append(value)
                bin_spaces[bin_name] -= value
                count += 1
                added = True
                del retlist[key]
            bin += 1
        if(not added):
            new_bin = "bin_" + str(binz)
            gamelist[new_bin] = [key]
            gamespace[new_bin] = [value]
            bin_spaces[new_bin] = ami_space - value
            count += 1
            binz += 1
            del retlist[key]

filename = "pop_group.csv"
f = open(filename, "w", encoding="utf-8")
headers = "Bin No, Games, Total Space\n"
f.write(headers)
for key,value in gamelist.items():
    bin_no = key
    games = ", ".join(value)
    tspace = "{:.2f}".format(sum(gamespace[key]))
    f.write( bin_no + "," + games + "," + tspace + "\n")

f.close()