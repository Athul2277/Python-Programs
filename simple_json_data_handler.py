import json

data = {"name": "Anil", "age": 21}

file = open("data.json", "w")
json.dump(data, file)
file.close()

file = open("data.json", "r")
loaded = json.load(file)
file.close()

print("Loaded Data:", loaded)
