from re import L
import pyttsx3
import speech_recognition as sr
def speak(audio):
    print("Alpha: " + audio)
    engine=pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

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