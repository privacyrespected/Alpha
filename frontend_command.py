#this files process commands entered through the front end
from modules.sense import *
from modules.mainsystem import *
def Pcommand(command):
    command=command.lower()
    if command.startswith("speak"): #speak function to debug
        command=command.replace("","speak")
        speak(command)
    elif command.startswith("shutdown"):
        speak("shutdown initiated")
    elif command.starswith("dns"):
        command = command.replace("","dns")
        if command.startswith("flush"):
            flushdns()
        else:
            speak("No param specified")
    elif command.startswith("kill"):
        kill()