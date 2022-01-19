import playsound

def startnoise1(): #this starts when training happens
    try:
        playsound("audio/start2.mp3")
    except Exception as e:
        print(e)
        return None

#these run simulataneously when the app can actually launch
def startupnoise():
    print("startupnoise initiated")
    try:
        playsound("audio/startup.mp3")
    except Exception as e:
        print(e)
        return None
def startupnoise2():
    try:
        playsound("audio/start3.mp3")
    except Exception as e:
        print(e)
        return None