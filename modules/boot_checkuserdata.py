from os import path
import json
import os
from tkinter import E
from sense import notify
import time
def checkuserdata():
    #this file checks for user data
    if path.isfile('data.json') == False:
        notify("OPPs!","Cant start without data.json, try again","60")
        time.sleep(30)
        exit()
    else:
        print("Loading user data.")
        try:
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
        except Exception as e:
            print(e)
            notify("OHNO", e, 90)
        return user_name, usercity, user_gender,user_dob, user_email,user_email_password, user_species, user_bloodtype,user_skincolor,user_ethnicity
