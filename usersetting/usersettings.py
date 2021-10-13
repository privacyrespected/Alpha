
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
#imports the notification system.
from win10toast import ToastNotifier

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

@eel.expose
def usersettingwrite(username, usercity, user_gender, userdob, useremail, useremailpass):
    try:       
        chatbot = ChatBot(
        'Alpha',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter',
            'chatterbot.logic.BestMatch',
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.90
            }
        ],
        database_uri='sqlite:///database.sqlite3'
        )
            # Training with Personal Ques & Ans 
        if path.isfile('usersetting/chatdata.txt') == False:
            dataconfirm = ToastNotifier()
            dataconfirm.show_toast("Alpha", "Essential files deleted, please reinstall", duration = 10)
            time.sleep(10)
            exit()
        elif path.isfile("usersetting/additionaldata.txt")==False:
            dataconfirm=ToastNotifier()
            dataconfirm.show_toast("Alpha","Essential files delted, please reinstall",duration=10)
            
        training_data_simple = open('usersetting/chatdata.txt').read().splitlines()
        training_data_personal = open('usersetting/additionaldata.txt').read().splitlines()

        training_data = training_data_simple + training_data_personal

        trainer = ListTrainer(chatbot)
        trainer.train(training_data) 
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
            dataconfirm.show_toast("Alpha", "User data confirmed.", duration = 10, icon_path ="app.ico")
            time.sleep(5)
            exit()
    except Exception as e:
        print(e)
if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:

    eel.start("homesetting.html",cmdline_args=['--start-fullscreen','--incognito'], port=1111, mode='default',  disable_cache=True,close_callback=close_callback,)
else:
    raise EnvironmentError('Error: System is not Windows 10 or above')
