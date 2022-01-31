from cv2 import mean
import wikipedia
from sense import speak
import re
from PyDictionary import PyDictionary
mean= PyDictionary()
def search_wiki(query):
    results= wikipedia.summary(query, sentences=2)
    results =str(results)
    results=re.sub("[\(\[].*?[\)\]]", "", results)
    speak(results)

def search_meaning(query):
    results=mean.meaning(query)
    results=str(results)
    if re.search(",",results):
        results=re.sub(",","( or)",results)
    speak("For the word "+ query)
    speak(results)

