from functions import *
from response import *
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
        #this line checks for unneccessary words that may confuse the bot
        for extracheck in extrawords:
            if extracheck in query:
                query=query.replace(extracheck,"")
                for check in articleseng:
                    if check in query:
                        query=query.replace(check,"")
            else:
                continue

        for sysinfotrigger in sysinfo:
            if sysinfotrigger in query:
                speak("Okay, here are your system information. Please wait a moment")
                file=open("user.txt","r")
                lines = file.readlines
                if "Male" in lines[6]:
                    speak("sir")
                else:
                    speak("Madam")
                os.system("systeminfo.exe")
        for calculator in calculate_triggger:
            if calculator in query:
                query=query.replace(calculator,"")
                query= str(query)
                print(eval_binary_expr(*(query.split())))
                speak(eval_binary_expr(*(query.split())))

        #the dictionary function
        if "meaning" in query:
            for check in meaningextrawords:
                if check in query:
                    query=query.replace(check,"")
                else:
                    dictionary(query)


        #the weather function
        elif "weather" in query:
            for check in prepsplace:
                if check in query:
                    query=query.replace(check,"")
                    for check in meaningextrawords:
                        if check in query:
                            query=query.replace(check,"")
                            weathermain(query)
                        else:
                            weathermain(usercity)
                else:
                    weathermain(usercity)
        
        #screenshot function
        elif "a screenshot" in query:
            screenshot()

        #news function
        elif "news" in query:
            getnews()
        
        #open youtbube
        elif 'youtube' in query:
            speak("Opening youtube")
            webbrowser.open("www.youtube.com")


        #check the time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            if user_gender == "Male":
                speak(f"Sir, the time is {strTime}")
            else:
                speak(f"Madam, the time is {strTime}")

        else:
            speak(random.choice(understandnt))
            understanderror="Unable to comprehend command: " +str(query)
            understanderror=str(understanderror)
            reporterror(understanderror, "try different voice commands")
            return







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