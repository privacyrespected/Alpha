#Import modules
from winreg import QueryValue
from modules.display import slowprint
from modules.display import ascii
from modules.bootloader import checkuserdata, startup_main
from modules.sense import listen, speak
from modules.chatgpt import chatgpt
from UI import alpha_frontend
from modules.weather import weathermain
from modules.mainsystem import *
import re
import spacy
nlp = spacy.load("en_core_web_sm")
####################################
#INTRO
results=ascii("ALPHA V 5.0")
print(results)
slowprint("Designed by PrivacyRespected in the United Kingdom")

######################################################################################
#GREET 
def alpha_main():
    startup_main()
    mute =0
    #######################################################################################
    while True:
        
        #reorganise the string into readable format
        test = str(listen())
        res=re.findall(r'\".*?\"', test)
        input = res[1]
        input =input.strip('\"')
        print(input)
        if input.startswith("hello"):
            input = input.replace("hello","")
            if input=="alpha":
                speak("How can I help you?")
            
            else:
                if input == "":
                    continue
                else:
                    print("USER INPUTL: "+ input)
                    print("Output: ") #comment this line 
                    #### continue all your shit below
                    if input.startswith("mute"):
                        mute =1
                        continue
                    if "weather" in input:
                        if "in " in input:
                            input_city= re.search("^in: (\w+)",input)
                            target=input_city.groups()
                            weathermain(target)
                        else:
                            weathermain(checkuserdata()[1])
                    elif "check" and "memory" in input:
                        checkram()
                    elif "check" and "cpu" in input:
                        checkcpu()
                    elif "check" and "battery" in input:
                        checkbattery()
                    elif "check" and "system" in input:
                        systemstats()
                    elif "flush" and "dns" in input:
                        flushdns()
                    elif input.startswith("shut down"):
                        speak("Shutdown protocol has been executed")
                        shutdown_s()
                    elif "kill program" in input:
                        kill()

                    else:
                        chatgpt(input)
        else:
            continue





alpha_main()