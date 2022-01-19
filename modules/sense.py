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
    notify= ToastNotifier()
    icon_path=None
    notify.show_toast(title, content, icon_path, duration)


