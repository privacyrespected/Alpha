import eel
import time
import os
from datetime import date
import datetime
import eel
import sys
import platform
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#with open('data.json', 'w', encoding='utf-8') as f:
    #json.dump(data, f, ensure_ascii=False, indent=4)

# Creating ChatBot Instance
chatbot = ChatBot(
    'Alpha',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

 # Training with Personal Ques & Ans 
training_data_simple = open('chatdata.txt').read().splitlines()
training_data_personal = open('personchatdata.txt').read().splitlines()

training_data = training_data_simple + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)


eel.init("usersetting/settingweb")

@eel.expose
def usersettingwrite(username, usercity, user_gender, userdob, useremail, useremailpass):
    try:        
        with open('data.json', 'w', encoding='utf-8') as f:
        #json.dump(data, f, ensure_ascii=False, indent=4)
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
    except Exception as e:
        print(e)
if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:

    eel.start("homesetting.html",cmdline_args=['--start-fullscreen'], port=1111, mode='default')
else:
    raise EnvironmentError('Error: System is not Windows 10 or above')
