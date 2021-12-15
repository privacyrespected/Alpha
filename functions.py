def reporterror(errorr, suggest):
    print(errorr + suggest)
#import modules
from win10toast import ToastNotifier
import pyttsx3
import speech_recognition as sr
import wikipedia
import re
import datetime
import requests
from pprint import pprint
import pyautogui
import psutil
import math
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
def listen():#debug version here
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

def screenshot():
    img = pyautogui.screenshot()
    img.save(r"C:\Users\Gabriel\Pictures\Camera Roll\ss.jpg")
    speak("Okay, it is now in your Pictures folder")
    
def checkram():
    memory_info= psutil.virtual_memory()
    output= str(memory_info.percent)
    speak("The current RAM usage is ")
    speak(output)
    speak("percent")

def checkcpu():
    checkcpu= psutil.cpu_percent()
    checkcpu=str(checkcpu)
    speak("The current CPU usage is ")
    speak(checkcpu)
    speak("percent")

def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']
    print(city)
    print(state)
    print(country)
    return city, state,country

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   print("%s %s" % (s, size_name[i]))
   return "%s %s" % (s, size_name[i])


def system_stats():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used and battery level is at {battery_percent} percent"
    return final_res

