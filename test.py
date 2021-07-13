import json
with open("data.json", "r") as read_file:
    data = json.load(read_file) 
    e=data["main_user_data"]
    f=e["username"]
    print(e)

    print(f)