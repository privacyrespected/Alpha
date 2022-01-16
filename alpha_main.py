from sre_constants import NOT_LITERAL_IGNORE
import external.interactions
from external.notify import notify, reporterror
import external.search_wikipedia
import external.systems
import external.weather
import os
import time
import eel
import psutil
import platform
import sys
import random
from threading import Thread
from os import path
import json
print("Alpha V3.0")
print("Alpha is a new virtual assistance built in attempt to replicate an intelligent human.")

eel.init("web")  
@eel.expose
#eel functions specifically for eel gui
def checkram():
    memory_info=psutil.virtual_memory()
    current_ram = "Ram: " + str(memory_info.percent)+"%"
    #uncomment to print and debug
    #print(current_ram)
    return current_ram
@eel.expose
def checkcpu():
    cpustat= psutil.cpu_percent()
    current_cpu= "CPU: " + str(cpustat)+"%"
    return current_cpu
@eel.expose
def checknetwork1():
    checknetwork= psutil.sensors_battery().percent
    checknetwork= str(checknetwork)
    current_network="Battery: " + checknetwork + "%"
    return current_network
def alpha_frontend():
    #check system 
    if sys.platform in ['win32','win64'] and int(platform.release()) >= 10:
        print("Start frontend")
        #start tthe frontend functions
        eel.start("index.html",cmdline_args=['--start-fullscreen'], port=4000)
    else:
        #ono error happened
        raise EnvironmentError('Error: System is not Windows 10 or above')
if path.isfile('data.json') == False:
    reporterror("data.json not found", "Run usersettings.exe please")
    reporterror("OPPs!","Cant start without data.json, try again","60")
    time.sleep(30)
    exit()
#user data reconfirmation in backend
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
        notify("Alpha",e,duration=10)
def alphamain():
    try:
        Thread(target=external.startup.startupnoise).start()
        Thread(target=external.startup.startupnoise2).start()
        Thread(target=external.startup.greet(user_name,user_gender)).start()
    except Exception as e:
        print(e)
        reporterror(e, "github it or ask a cat")

#initiate functions
if __name__ == "__main__":
    print("started")
    try:
        Thread(target=alphamain).start()
        Thread(target=alpha_frontend).start()
    except Exception as e:
        print(e)
        reporterror(e, "github it or ask a cat")