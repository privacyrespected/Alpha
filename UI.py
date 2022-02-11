#This program is used for linkage of the UI to the backend algorithm such as the live computer stats shown on the left menu

from platform import platform
import eel
import psutil
import sys
import platform
from frontend_command import Pcommand
eel.init("web")
@eel.expose
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
    current_network="Energy: " + checknetwork + "%"
    return current_network
@eel.expose
def checkcommand(commandinput):
    print(commandinput)
    Pcommand(commandinput)
    

#frontend functions
def alpha_frontend():
    if sys.platform in ['win32', 'win64'] and int(platform.release())>=10:
        eel.start("index.html",  cmdline_args=['--start-fullscreen'],port=4000)
    else:
        raise EnvironmentError("Error: system is not windows 10 or above")

#uncomment this line to purely debug this function
#alpha_frontend()
alpha_frontend()
