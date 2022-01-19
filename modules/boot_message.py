import time
from datetime import datetime
from sense import speak
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
