from playsound import playsound
import time
import external.notify
import random
import datetime
from external.interactions import speak
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
def play_startup_noise2():
    try:
        playsound("audio/start2.mp3")
    except Exception as e:
        print(e)
def startupnoise():
    print("startupnoise initiated")
    try:
        playsound("audio/startup.mp3")
    except Exception as e:
        external.notify.reporterror("Cannt find file in directory","check if all files are properly installed")
def startupnoise2():
    try:
        playsound("audio/start3.mp3")
    except Exception as e:
        print(e, "audio problems, please check your audio related components")
def greet(user_name,user_gender):
    time.sleep(1)
    print(random.randint(1,2))
    random_functions = random.randint(1,2)
    if int(random_functions) == 1:
        wishMe(user_gender)
    elif int(random_functions) == 2:
        wishme2(user_name)
    else:
        external.notify.reporterror("big shit happened","report it on github code=001")
