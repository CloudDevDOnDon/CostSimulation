import pandas as pd
import math

instance_count = 0
instance_hours = {} #how many AWS hours in total, need to initialize to 0
available = [] #contain instanceId
occupied = {} #contain userId, instanceId [0], time start used [1]


def get_instance(userId, timestamp):
	global instance_count
	global instance_seconds
	global instance_hours
	global available
	global occupied

	if (len(available) == 0):
		instance_count += 1
		occupied[userId] = [instance_count, timestamp]
		instance_hours[instance_count] = 0
	else:
		occupied[userId] = [available[0], timestamp]
		available.pop(0)

def release_instance(userId, timestamp):
	global instance_count
	global instance_seconds
	global instance_hours
	global available
	global occupied

	ins = occupied[userId][0]
	instance_hours[ins] += math.ceil((timestamp - occupied[userId][1])/3600)
	available.append(ins)
	del occupied[userId]

def main():
	df_sorted = pd.read_csv("./dataset.txt", sep=" ")
	print(df_sorted)

	for index, row in df_sorted.iterrows():
		print(index, row)
		if(row["action"] == "start"):
			get_instance(row["id"], row["timestamp"])
		elif(row["action"] == "end"):
			release_instance(row["id"], row["timestamp"])

	instances = list(instance_hours.keys())
	instances.sort()
	for ins in instances:
		print("Instance number: " + str(ins) + ", Hours: " + str(instance_hours[ins]))

	# active = []
	# o = open("./wow_cleaned_final.txt","w")

	# data = pd.read_csv("./WoWSessionData.txt", sep=", ")
	# filtered = data.loc[data['Event'].isin(["PLAYER_LOGIN","PLAYER_LOGOUT"])]
	# sorted_filtered = filtered.sort_values(by=['Timestamp'])

	# print(sorted_filtered)

	# o.write("id action timestamp\n")

	# for index, row in sorted_filtered.iterrows():
	# 	print(index, row)
	# 	if(row["Category"] == "SESSION_START"):
	# 		if (row["PlayerID"] in active):
	# 			continue
	# 		else:
	# 			active.append(row["PlayerID"])
	# 			o.write(str(row["PlayerID"]) + " start " + str(int(row["Timestamp"])) + "\n")

	# 	elif(row["Category"] == "SESSION_END"):
	# 		if (row["PlayerID"] not in active):
	# 			continue
	# 		else:
	# 			active.remove(row["PlayerID"])
	# 			o.write(str(row["PlayerID"]) + " end " + str(int(row["Timestamp"])) + "\n")

	# for playerId in active:
	# 	o.write(str(playerId) + " end " + str(1246657574) + "\n")
	# 	active.remove(playerId)

	# print(active)

if __name__ == '__main__' :
	main()