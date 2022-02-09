#this files process commands entered through the front end
from modules.sense import *
def Pcommand(command):
    command=command.lower()
    if command.startswith("speak"): #speak function to debug
        command=command.replace("","speak")
        speak(command)