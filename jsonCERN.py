import json

f = open("wlcg.json")
data = json.load(f)
total = 0

for entry in data:
	if entry["PledgeType"] == "Disk" and entry["Country"] == "Germany" and entry["ATLAS"] != "":
		print(entry["Federation"] + ": " + str(entry["ATLAS"]) + " " + entry["PledgeUnit"])
		total += int(entry["ATLAS"])
		
print("Total: " + str(total))
