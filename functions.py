def reporterror(errorr, suggest):
    print(errorr + suggest)
#import modules
from win10toast import ToastNotifier
import pyttsx3
import speech_recognition as sr
import wikipedia
import re
import datetime
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
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening>>>")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing: ")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        print(e)
        print("Audio not heard, plesae try again")
        return "None"
    return query
#wikipedia search
def wikipedia(query):       
    try:
        print(query)
        output=wikipedia.search(query,results=4, suggestion =True)
        output2=wikipedia.search(query,sentences=3)
        output=output.lower()
        output2=output2.lower()
        speak(output2)
        if re.findall(query, output): #this line checks if there are any duplicates
            output=query.replace(output,"")
            speak("Fancy of more details? Here are some other topics suggested")
            speak(output)
        else:
            speak('Fancy of more details? Here are some other topics suggested')
            speak(output)
    except Exception as e:
        reporterror(e, "Contact developer")
    
#wishme functions only for startup boot
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    file=open("user.txt","r")
    file.readlines
    if "Male" in lines[6]:
        speak("I am Alpha! Sir, Please tell me how may I help you")
        print("I am Alpha")
    else:
        speak("I am Alpha! Madam, please tell me how may I help you.")       
def wishme2():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        speak( user_name + "What are you planning to do?" )
    
    elif hour>=12 and hour<18:
        speak("Good afternoon, ready to continue work?")
    else:
        speak("Good evening! " + user_name)
        speak("How is your day?")
