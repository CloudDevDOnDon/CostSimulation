import pandas as pd
import math

instance_count = 0
instance_seconds = {} #how many seconds used nonstop [0] and time started running [1], need to initialize to 0
instance_hours = {} #how many AWS hours in total, need to initialize to 0
available = {} #contain instanceId, time last used [0], and extra time [1]
occupied = {} #contain userId, instanceId [0], and time start used [1]
lambda_count = 0
duration = []

def get_instance(userId, timestamp):
	global instance_count
	global instance_seconds
	global instance_hours
	global available
	global occupied
	global lambda_count

	if (len(available) == 0):
		instance_count += 1
		occupied[userId] = [instance_count, timestamp]
		instance_seconds[instance_count] = [0, timestamp]
		instance_hours[instance_count] = 0
	else:
		max_extra = -1
		max_ins = None
		for ins in available.keys():
			if (available[ins][1] != 0):
				if ((timestamp - available[ins][0]) > available[ins][1]):
					lambda_count += 1
					instance_hours[ins] += math.ceil(instance_seconds[ins][0]/3600)
					instance_seconds[ins] = [0, None]
					available[ins][1] = 0
			if (available[ins][1] > max_extra):
				max_extra = available[ins][1]
				max_ins = ins
		occupied[userId] = [max_ins, timestamp]
		if (instance_seconds[max_ins][1] == None):
			instance_seconds[max_ins] = [0, timestamp]
		del available[max_ins]

def release_instance(userId, timestamp):
	global instance_count
	global instance_seconds
	global instance_hours
	global available
	global occupied
	global duration

	ins = occupied[userId][0]
	instance_seconds[ins][0] = timestamp - instance_seconds[ins][1]
	extra_time = (3600-(instance_seconds[ins][0]%3600))
	available[ins] = [timestamp, extra_time]
	duration.append(timestamp - occupied[userId][1])
	del occupied[userId]

def main():
	global instance_seconds
	global instance_hours
	global available
	global lambda_count
	global duration

	df_sorted = pd.read_csv("./dataset.txt", sep=" ")
	print(df_sorted)

	for index, row in df_sorted.iterrows():
		# print(index, row)
		if(row["action"] == "start"):
			get_instance(row["id"], row["timestamp"])
		elif(row["action"] == "end"):
			release_instance(row["id"], row["timestamp"])

	for ins in available.keys():
		if (available[ins][1] != 0):
			lambda_count += 1
			instance_hours[ins] += math.ceil(instance_seconds[ins][0]/3600)
			instance_seconds[ins] = [0, None]
			available[ins][1] = 0

	instances = list(instance_hours.keys())
	instances.sort()
	total = 0
	for ins in instances:
		total += instance_hours[ins]
		print("Instance number: " + str(ins) + ", Hours: " + str(instance_hours[ins]))

	print("Lambda function triggered " + str(lambda_count) +  " times")
	print("Average duration = " + str(sum(duration)/len(duration)) + "s")
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