def reporterror(errorr, suggest):
    print(errorr + suggest)
#import modules
from win10toast import ToastNotifier
import pyttsx3
import speech_recognition as sr
import wikipedia
import re
import datetime
#notify functiion
def notify(title, content, duration):
    dataconfirm = ToastNotifier()
    icon_path="app.ico"
    dataconfirm.show_toast(title, content, duration, icon_path)


#tts
def speak(audio):
    print(audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
#speech recognition
def listen():
    query=input("Input command to start debugging: ")
    return query
#wikipedia search
def swikipedia(query):       
    try:
        print(query)
        output2=wikipedia.summary(query,sentences=3)
        output2=str(output2)
        output2=output2.lower()
        #this parts removes brackets because they happen to be irrelavant
        output2= output2.replace("(","{")
        output2=output2.replace(')','}')
        output2= re.sub('{[^}]*}', '', output2)
        speak(output2)
    except Exception as e:
        reporterror(e, "Contact developer")
    
#wishme functions only for startup boot
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
        speak( user_name + "What are you planning to do?" )
    
    elif hour>=12 and hour<18:
        speak("Good afternoon, ready to continue work?")
    elif hour>18 and hour<22:
        speak("Good evening! " + user_name)
        speak("What are you planning to do?")
    else:
        speak("Good evening!" + user_name)
        speak("How was your day?")

import requests
from pprint import pprint
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=5bddd4ad4f4f192f6dfffe714388c103');
	return res.json();
def print_weather(result,usercity):
    
    speak("{}'s temperature is {} degress Celcius ".format(usercity,result['main']['temp']-273))
    speak("Wind speed is {} meters per second".format(result['wind']['speed']))
	
    speak("The weather looks {}".format(result['weather'][0]['description']))
	
    print("Weather: {}".format(result['weather'][0]['main']))
def weathermain(usercity):
    try:
        query='q='+usercity;
        w_data=weather_data(query);
        print_weather(w_data, usercity)
        print()
    except:
        print('City name not found...')

