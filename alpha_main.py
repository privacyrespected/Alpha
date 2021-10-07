from functions import *
from response import *
import re
print("ALPHA V2.0")
print("Developed by: NuggetCat ")
print("Email: nuggetcatsoftware@gmail.com")

import eel
#eel function link
eel.init("web")  

@eel.expose
#eel functions specifically for eel gui
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
    current_network="Battery: " + checknetwork + "%"
    return current_network


#this function starts eel frontend
def alpha_frontend():
    #check system 
    if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
        print("Start frontend")
        #start tthe frontend functions
        eel.start("index.html",cmdline_args=['--start-fullscreen'], port=4000, mode='default')
    else:
        #ono error happened
        raise EnvironmentError('Error: System is not Windows 10 or above')


def alphamain():
    while True:
        query= listen().lower()
        #MAKE SURE YOU DONT CAPLOCK IF CONDITIONS OR SHIT WONT WORK KEKW
        #this line reduces errors and warnings for "cant listen" and doesnt breaks the program

        #checks if its a function call and remind itself later 
        #because we will be deleting this string from query while processing it
        
        if query.startswith("can you"):
            var_function_call="True"
        else:
            continue


        #failsafe codes
        #puncuation problems that can commonly cause problems
        for punc in puncuations:
            if punc :
                query=re.sub(punc,"", query)
            else:
                continue
        #deletes additional spaces that causes problems
        if re.search("  ",query):
            query=re.sub("  ","",query)
        else:
            continue
        
        #These lines removes confusing/unnecessary words from query so that it can be understood easily
        for extra in extrawords:
            if re.search(extra,query):
                re.sub(extra,"",query)
            else:
                continue
        print(query)
        #Part A functional codes
        
        #Part A1. definitions code sector
        #A1.1: Indirect function calls (calls the function but  in a more human way)
        #needs to be coded
        for indirectvar in indirect_func_call_meaning:
            if indirectvar in query:
                re.sub(indirectvar,"",query)
                try:
                    dictionary(query)
                except Exception as e:
                    if user_gender=="Male":
                        speak(f"Apologies sir, I am unable to search the definition for {query}.")
                    else:
                        speak(f"Sorry Madam, I am unable to search the definition for {query}")
            else:
                continue     
        print(query)
        #A1.2: Direct function call (calls dictionary function on command)
        #dictionary
        if query.startswith("dictionary"):
            re.sub("dictionary","",query)
            dictionary(query)
        elif query.startswith('wikipedia'):
            re.sub("wikipedia","",query)
            wikipedia(query)

        #no such thing for wikipedia as wikipedia isn't a verb and cannot be used in indirect function call
        elif query.startswith("what") or query.startswith("define"): #add a line for indirect function call
            if re.search("what",query):
                re.sub("what","",query)
            #replaces the word what
            if query.startswith("is"): #this is the is conditionss
                re.sub("is","",query)    
                for art in articleseng:
                    if query.startswith(art):
                        #what is an apple situation
                        re.sub(art,"",query)
                        try:
                            dictionary(query)
                        except Exception as e:
                            print(e)#if this doesn't work this will!
                            wikipedia(query)#hopefully
                    else:
                        continue
                #is condition 2!! #is meaning condition
                for mean in meaningvar:
                    if query.startswith(mean):
                        re.sub(mean,"",query)
                        try:
                            dictionary(query)
                        except Exception as e:
                            print(e)#if this doesn't work this will!
                            wikipedia(query)#hopefully

#initiate functions
if __name__ == "__main__":
    print("started")
    import random
    print(random.randint(1,2))
    random_functions = random.randint(1,2)
    if int(random_functions) == 1:
        wishMe()
    elif int(random_functions) == 2:
        wishme2()
    try:
        Thread(target=alphamain).start()
        Thread(target=alpha_frontend).start()
    except Exception as e:
        print(e)
        reporterror(e, "github it or ask a cat")