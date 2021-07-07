import pandas as pd
import math

instance_count = 0
instance_hours = {} #how many AWS hours in total, need to initialize to 0
available = {} #contain AMI tagged => instanceId[0], 
occupied = {} #contain userId => instanceId [0], time start used [1]

def get_instance(userId, timestamp, gameID):
	global instance_count
	global instance_seconds
	global instance_hours
	global available
	global occupied

	"""
	example of available:
	
	{gameID: [InstanceID]}

	"""

	if gameID in available:
		if (len(available[gameID]) == 0):
			instance_count += 1
			# saved gameID in occupied for the release function
			occupied[userId] = [instance_count, timestamp, gameID]
			instance_hours[instance_count] = 0
		else:
			# Tracking games played by the user.
			occupied[userId] = [available[gameID][0], timestamp, gameID]
			available[gameID].pop(0)
	else:
		instance_count += 1
		occupied[userId] = [instance_count, timestamp, gameID]
		instance_hours[instance_count] = 0
	# print(f"Get Instance: {available}")

def release_instance(userId, timestamp):
	global instance_count
	global instance_seconds
	global instance_hours
	global available
	global occupied

	ins = occupied[userId][0]
	instance_hours[ins] += math.ceil((timestamp - occupied[userId][1])/3600)
	# If the instance ID already exist, append else create new key and append
	if occupied[userId][2] in available:
		available[occupied[userId][2]].append(ins)
	else:
		available[occupied[userId][2]] = [ins]
	del occupied[userId]

	# print(f"Release Instance: {available}")


def main():
	# Read a different dataSet to differenciate between single/ multi AMI
	df_sorted = pd.read_csv("./newDataSet.txt", sep=" ")
	# print(df_sorted)

	for index, row in df_sorted.iterrows():
		# print(index, row)
		if(row["action"] == "start"):
			# Added an additional column with information regarding what each users wish to play
			get_instance(row["id"], row["timestamp"], int(row['GameID']))
		elif(row["action"] == "end"):
			release_instance(row["id"], row["timestamp"])

	instances = list(instance_hours.keys())
	instances.sort()
	total = 0
	for ins in instances:
		total += instance_hours[ins]
		print("Instance number: " + str(ins) + ", Hours: " + str(instance_hours[ins]))
		#print(str(instance_hours[ins]))

	print(f"Total Hours: {total}")

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