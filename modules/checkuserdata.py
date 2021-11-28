from os import path
import os
import time
import json
from modules.reporterror import reporterror
#load user data functions
print("Checking user data...")
if path.isfile('data.json') == False:
    reporterror("User.txt not found", "Run usersettings.exe please")
    os.startfile("hmm.vbs")
    time.sleep(30)
    exit()
#user data reconfirmation in backend
print("Loading user data.")
with open("data.json", "r") as read_file:
    userdata = json.load(read_file) 
    main_data=userdata["main_user_data"]
    user_name=main_data["username"]
    usercity=main_data["usercity"]
    user_gender=main_data["usergender"]
    user_dob=main_data["userdob"]
    user_email=main_data["useremail"]
    user_email_password=main_data["useremailpass"]
    user_species=main_data["userspecies"]
    user_bloodtype=main_data["userbloodtype"]
    user_skincolor=main_data["userskincolor"]
    user_ethnicity=main_data["userethnicity"]
    user_religion=main_data["userreligion"]
    user_weight=main_data["userweight"]
    user_height=main_data["userheight"]
    user_sport=main_data["usersport"]
    user_hobby=main_data["userhobby"]
    user_interest=main_data["userinterest"]
    user_discord=main_data["userpersonaldiscordbottoken"]
    print("Confirming user data")
    print(user_name)
    print(usercity)
    print(user_gender)
    print(user_dob)
    print(user_email)
    print(user_email_password)
    print(user_species)
    print(user_bloodtype)
    print(user_skincolor)
    print(user_ethnicity)
    print("All data confirmed and detected")