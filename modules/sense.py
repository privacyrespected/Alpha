import time
import pyttsx3
import speech_recognition as sr
from win10toast import ToastNotifier
#tts
def speak(audio):
    print("Alpha: "+audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

#listen
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
        print(f"User:  {query}\n")
    except Exception as e:
        print(e)
        print("Audio not heard, plesae try again")
        return "None"
    if query is None:
        print("audio not heard at thres 2")
    else:
        return query

def notify(title, content, duration):
    ctime= time.ctime()
    file=open("error.txt","w")
    file.write(ctime)
    file.write("\n")
    file.write(title)
    file.write("\n")
    file.write(content)
    file.write("\n")
    file.write(duration)
    file.write("\n")
    file.close()

