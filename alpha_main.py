try:
    from functions import *
    from response import *
    import re
    import regex
    from os import path
    import os
    import time
    import json
    import psutil
    import platform
    import sys
    from threading import Thread
    import random
    from chatterbot import ChatBot
    from chatterbot.trainers import ListTrainer
    from chatterbot.trainers import ChatterBotCorpusTrainer
except Exception as e:
    reporterror(e, "that shouldn't happen. Please contact the developer")

print("ALPHA V3.0")
print("Developed by: NuggetCat ")
print("Email: nuggetcatsoftware@gmail.com")
print("For update logs please view it on github of this repo")
print("Checking user data...")

###Chatbot variables definition
chatbot=ChatBot("Alpha", logic_adapters=[
    'chatterbot.logic.BestMatch',
    'chatterbot.logic.TimeLogicAdapter',
    'chatterbot.logic.MathematicalEvaluation'
])

trainer=ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.ai"
)
trainer=ListTrainer(chatbot)
trainer.train(conversation)
#####

if path.isfile('data.json') == False:
    reporterror("data.json not found", "Run usersettings.exe please")
    notify("OPPs!","Cant start without data.json, try again","60")
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
        # create an object to ToastNotifier class
        dataconfirm = ToastNotifier()
        dataconfirm.show_toast("Alpha", "User data confirmed", duration = 5, icon_path ="app.ico")
    except Exception as e:
        print(e)
        shit=ToastNotifier()
        shit.show_toast("Alpha", e, duration=10, icon_path="app.ico")
import eel
#eel function link
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


#this function starts eel frontend
def alpha_frontend():
    #check system 
    if sys.platform in ['win32','win64'] and int(platform.release()) >= 10:
        print("Start frontend")
        #start tthe frontend functions
        eel.start("index.html",cmdline_args=['--start-fullscreen'], port=4000)
    else:
        #ono error happened
        raise EnvironmentError('Error: System is not Windows 10 or above')


def alphamain():
    #greet the user
    #put here such that frontend function and backend function can run simultaneously

    print(random.randint(1,2))
    random_functions = random.randint(1,2)
    if int(random_functions) == 1:
        wishMe(user_gender)
    elif int(random_functions) == 2:
        wishme2(user_name)
    else:
        reporterror("big shit happened","report it on github code=001")

    #loop for listenin
    while True:
        query=listen() #lowered for simpler regex processing (hopefully)
        query= str(query)
        query=query.lower()
        #SENTENCE CLEANUP (REMOVAL OF SOME EXTRA WORDS)
        for cleanup in extrawords:
            if re.findall(cleanup,query):
                query =re.sub(cleanup,"",query)
            else:
                continue
        #################

#### If statements starts here

        #DIRECT FUNCTION CALLS
        #check wikiedpia
        if re.findall("^wikipedia", query):
            query=re.sub("wikipedia","",query)
            swikipedia(query)
        #check weather
        elif re.findall("^weather", query):
            if "my location" in query:
                city, state,country= my_location()
                city=str(city)
                weathermain(city)
            else:
                query=re.sub("weather","",query)
                weathermain(query)
        #take screenshot
        elif re.findall("^screenshot",query):
            screenshot()
        #check system stats
        elif re.findall("^check",query):
            print("data check")
            query=re.sub("check","",query)
            print(query)
            if query.startswith("ram"):
                checkram()
                print("check RAM")
            elif query.startswith("cpu"):
                checkcpu()
            elif query.startswith("network"):
                print("network check") #to be added
        #system actions
        elif re.findall("^system",query):
            query=re.sub("system","",query)
            print(query)
            stat=[
                "stats",
                "stat",
                "statistics"
            ]
            for s in stat:
                if s in query:
                    final_res=system_stats()
                    str(final_res)
                    speak(final_res)
                else:
                    print("no stat :(")
                    continue
            if "shutdown" in query:
                speak("initiating shutdown procedure")
                os.system('shutdown -s')
            
            elif "restart" in query:
                speak("Initiating reboot procedure")
                os.system("shutdown -r")

        
        #QUESTION BASED RESPONSES


        #human interactions
        else:
            print("Human responses (from chatterbot)")
            response=chatbot.get_response(query)
            speak(response)
            trainer.export_for_training("./conversation_data.json")



#initiate functions
if __name__ == "__main__":
    print("started")
    try:
        Thread(target=alphamain).start()
        Thread(target=alpha_frontend).start()
    except Exception as e:
        print(e)
        reporterror(e, "github it or ask a cat")