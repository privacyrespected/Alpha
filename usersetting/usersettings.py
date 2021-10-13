from logging import disable
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
#imports the notification system.
from win10toast import ToastNotifier
#imports chatbot modules and functions
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
def close_callback():
    dataconfirm = ToastNotifier()
    dataconfirm.show_toast("Alpha", "Data not yet confirmed, please try again", duration = 10, icon_path ="app.ico")
    if path.isfile('data.json') == False:
        exit()
    else:
        os.remove("data.json")
        time.sleep(1)
        exit()

#start the eel session
eel.init("usersetting/settingweb")
#screen loading session for machine learning chatterbot
def loading():
    #loading problems
    def close_callbackload():
        dataconfirm = ToastNotifier()
        dataconfirm.show_toast("Alpha", "Data not yet confirmed, please try again", duration = 10, icon_path ="app.ico")
        if path.isfile('data.json') == False:
            exit()
        else:
            os.remove("data.json")
            exit()

    eel.start(eel.start("homesetting.html",block=False,cmdline_args=['--start-fullscreen','--incognito'], port=1111, mode='default',  disable_cache=True,close_callback=close_callbackload,))



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
            json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
            #notifies the user that 
            dataconfirm = ToastNotifier()
            dataconfirm.show_toast("Alpha", "User data confirmed. Program will kill itself in 10 seconds", duration = 10, icon_path ="app.ico")
            time.sleep(10)
            exit()
    except Exception as e:
        print(e)
if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:

    eel.start("homesetting.html",cmdline_args=['--start-fullscreen','--incognito'], port=1111, mode='default',  disable_cache=True,close_callback=close_callback,)
else:
    raise EnvironmentError('Error: System is not Windows 10 or above')
