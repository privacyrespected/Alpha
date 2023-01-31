#speak
#listen
#notify
import time
import pyttsx3
import speech_recognition as sr
from win10toast import ToastNotifier
import argparse
import queue
import sys
import sounddevice as sd
from vosk import Model, KaldiRecognizer
#tts
def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty("volume", 1)
    engine.say(audio)
    engine.runAndWait()

#listen 
#reimplement anther system
#def listen():
#    r = sr.Recognizer()
#    with sr.Microphone() as source:
#        print("Listening>>>")
#        r.pause_threshold = 1
#        r.adjust_for_ambient_noise(source)
#        audio = r.listen(source)
#
#    try:
#        print("Recognizing: ")
#        query = r.recognize_google(audio, language='en-in')
#        print(f"User:  {query}\n")
#    except Exception as e:
#        print(e)
#        print("Audio not heard, plesae try again")
#        return "None"
#    if query is None:
#        print("audio not heard at thres 2")
#    else:
#        return query

q= queue.Queue()
def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))
def listen():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-l", "--list-devices", action="store_true",
        help="show list of audio devices and exit")
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        "-f", "--filename", type=str, metavar="FILENAME",
        help="audio file to store recording to")
    parser.add_argument(
        "-d", "--device", type=int_or_str,
        help="input device (numeric ID or substring)")
    parser.add_argument(
        "-r", "--samplerate", type=int, help="sampling rate")
    parser.add_argument(
        "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
    args = parser.parse_args(remaining)

    try:
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, "input")
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info["default_samplerate"])
            
        if args.model is None:
            model = Model(lang="en-us")
        else:
            model = Model(lang=args.model)

        if args.filename:
            dump_fn = open(args.filename, "wb")
        else:
            dump_fn = None

        with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device,
                dtype="int16", channels=1, callback=callback):
            print("#" * 80)
            print("Press Ctrl+C to stop the recording")
            print("#" * 80)

            rec = KaldiRecognizer(model, args.samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    output=rec.Result()
                    return output
                if dump_fn is not None:
                    dump_fn.write(data)
                else:
                    continue #we need to find a way to eliminate this line
                
    except KeyboardInterrupt:
        print("\nDone")
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ": " + str(e))



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

