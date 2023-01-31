#DO NOT RUN THIS MODULE INDIVIDUALLY
#This is the main startup function
#It only runs when the program is started
import json
from os import path
from modules.sense import speak
import time
from modules.display import slowprint
import datetime
import random
from playsound import playsound
from threading import Thread

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

#check user data
def checkuserdata():
    if path.isfile('data.json')==False:
        speak('File for data.json is not found, please rerun setup configurations')
        time.sleep(1)
        exit()
    else:
        print("Loading user data")
        try:
            with open("data.json","r") as read_file:
                userdata=json.load(read_file)
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
            speak(e)
        return user_name, usercity, user_gender,user_dob, user_email,user_email_password, user_species, user_bloodtype,user_skincolor,user_ethnicity

def startup_speak():
    user_name= checkuserdata()[0]
    user_gender=checkuserdata()[2]
    randomfunction = random.randint(1,2)
    if int(randomfunction)==1:
        wishMe(user_gender)
    elif int(randomfunction)==2:
        wishme2(user_name)
    else:
        speak("what the fuck?")
def startup_audio():
    playsound("audio/beep.mp3")

def startup_main():
    Thread(target=startup_speak).start()
    Thread(target=startup_audio).start()

