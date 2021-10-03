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
        #this line reduces errors and warnings for "cant listen" and doesnt breaks the program
        if query is None:
            print("Null query received, looping")
            continue
            #continue listening until else statement is fulfilled
        else:
            #puncuation problems that can commonly cause problems
            for punc in puncuations:
                if re.search(punc, query):
                    query=re.sub(punc,"", query)
                else:
                    continue
            #deletes additional spaces that causes problems
            if "  " in query:
                query=re.sub("  ","",query)
            else:
                continue
            #this line checks for unneccessary words that may confuse the bot
            for extra in extrawords:
                if re.search(extra, query):
                    query=re.sub(extra, "", query)
                else:
                    continue
            #this line defines the logic path for questions that demands a definition
            #what condition... what has too many possible combinations
            if re.search("what", query):
                query=re.sub("what","",query)
                #meaning condition-checks for the word meaning and run a definition search
                for m in mean:
                    if re.search(m,query):
                        for d in do:
                            if re.search(d, query):
                                query=re.sub(d,"",query)
                                    
                                




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