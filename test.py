import json
with open("data.json", "r") as read_file:
    data = json.load(read_file) 
    print(data)