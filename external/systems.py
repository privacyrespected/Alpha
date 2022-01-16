import math
import psutil
from interactions import speak
import pyautogui
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

def screenshot():
    img = pyautogui.screenshot()
    img.save(r"screenshots/screenshot.jpg")
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