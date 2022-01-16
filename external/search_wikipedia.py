import wikipedia
import re
from external.notify import notify
from interactions import speak
from notify import notify
def swikipedia(query):       
    try:
        print(query)
        output2=wikipedia.summary(query,sentences=3)
        output2=str(output2)
        output2=output2.lower()
        #this parts removes brackets because they happen to be irrelavant
        output2= output2.replace("(","{")
        output2=output2.replace(')','}')
        output2= re.sub('{[^}]*}', '', output2)
        speak(output2)
    except Exception as e:
        notify(e, "Contact developer")