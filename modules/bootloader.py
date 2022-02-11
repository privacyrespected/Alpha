import asyncio
from sys import modules
from threading import Thread
from playsound import playsound
import time
from sense import notify
import random
from sense import speak
import json
from os import path
import datetime

def wishMe(user_gender):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    if user_gender=="Male":
        speak("I am Alpha! Sir, Please tell me how may I help you")
        print("I am Alpha")
    else:
        speak("I am Alpha! Madam, please tell me how may I help you.")       
def wishme2(user_name):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        speak( user_name)
        speak("what are youh planning to do")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon, ready to continue work?")
    elif hour>18 and hour<22:
        speak("Good evening! " )
        speak(user_name)
        speak("What are you planning to do?")
    else:
        speak("Good evening!" )
        speak(user_name)
        speak("How was your day?")


def checkuserdata():
    #this file checks for user data
    if path.isfile('data.json') == False:
        notify("OPPs!","Cant start without data.json, try again",60)
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
        except Exception as e:
            print(e)
            notify("OHNO", e, 90)
        return user_name, usercity, user_gender,user_dob, user_email,user_email_password, user_species, user_bloodtype,user_skincolor,user_ethnicity
        

def startup1():
    user_name=checkuserdata()[0]
    user_gender=checkuserdata()[2]
    random_functions = random.randint(1,2)
    if int(random_functions) == 1:
        wishMe(user_gender)
    elif int(random_functions) == 2:
        wishme2(user_name)
