
from logging import disable
from bottle import load
import eel
import time
import os
from datetime import date
import datetime
import eel
import sys
import platform
import json
from os import path
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from modules.sense import speak
#imports the notification system.
from win10toast import ToastNotifier

#start the eel session
eel.init("usersetting/settingweb")
#screen loading session for machine learning chatterbot
@eel.expose
def usersettingwrite(username, usercity, user_gender, userdob, useremail, useremailpass):
    try:       
        with open('data.json', 'w', encoding='utf-8') as f:
            print("Name: " + username)
            print("Usercity: " + usercity)
            print("usergender: " + user_gender)
            print("userdob: " + userdob)
            print("useremail: " + useremail)
            print("useremailpass: " + useremailpass)
            data = {
                "main_user_data": {
                    "username": username,
                    "usercity": usercity,
                    "usergender":user_gender,
                    "userdob": userdob,
                    "useremail":useremail,
                    "useremailpass":useremailpass,
                    "userspecies": "homo sapien",
                    "userbloodtype": "null",
                    "userskincolor":"null",
                    "userethnicity":"null",
                    "userreligion":"null",
                    "userweight":"null",
                    "userheight":"null",
                    "usersport":"null",
                    "userhobby":"null",
                    "userinterest":"null",
                    "userpersonaldiscordbottoken":"null",
                    "dictpref":"british"
                }
            }
            speak("Please wait while we load your data")
            json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
            #notifies the user that 
            speak("Data loaded and confirmed")
            exit()
    except Exception as e:
        print(e)
if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:

    eel.start("homesetting.html",cmdline_args=['--start-fullscreen','--incognito'], port=1111, mode='default',  disable_cache=True)
else:
    raise EnvironmentError('Error: System is not Windows 10 or above')
