from pyautogui import screenshot
import psutil
from sense import speak
import requests
import os
#this program defines all possible ways to access computer statistic
#will expand to other devices connected in the long future we do not kno

#system information functions goes here
def checkram():
    memory_info=psutil.virtual_memory()
    output=str(memory_info.percent)
    speak("The current ram usage is ")
    speak(output)
    speak("percent")

def checkcpu():
    checkcpu=psutil.cpu_percent()
    checkcpu=str(checkcpu)
    speak("The current CPU usage is ")
    speak(checkcpu)
    speak("percent")

def checkbattery():
    battery_percent=psutil.sensors_battery().percent
    battery_percent=str(battery_percent)
    speak("The current battery percentage is")
    speak(battery_percent)
    speak("percent")

def systemstats():
    checkram()
    checkcpu()
    checkbattery()

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
#call it by my_location().city

def shutdown_s():
    os.system("shutdown/s /t 1")
#make sure you warn user before calling this function, may cause consequences

def flushdns():
    os.system('ipconfig/flushdns')
    speak("DNS flushed")

def kill():
    speak("killing program")
    exit()