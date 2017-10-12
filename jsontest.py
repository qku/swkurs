import json
f = open('ex.json')
a = json.load(f)
print(a)
print(a['Nummer'])
print(a['Inhaber']['Alter'])
