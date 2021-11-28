import pyttsx3
def speak(audio):
    print(audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()