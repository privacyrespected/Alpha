#this file is used to group ALL parts of the program into one file
#Compile only this file as all others are just functions and only this file can call it
print("Alpha V3")
print("nuggetcatsoftware@gmail.com")

#import modules for chatterbot
from logging import shutdown
from threading import Thread
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from corpus.customcorpus import * #imports the local corpus
from chatterbot import preprocessors
from modules.bootloader import startup1
#this line implements the custom chattebot preprocessors for extra word filter
from preprocessors import clean_words
###############

#importing modules from modules files
from modules.sense import *
from modules.mainsystem import *
from modules.search import *
from modules.weather import *
################
#importing modules for the UI
from UI import alpha_frontend

#import extra modules
from playsound import playsound

####
from modules.bootloader import *
extrawords=[
    "please",
    "would you mind",
    "do you mind",
    "tell me",
    "let me know",
    "you",
    "telling me",
    "can you"
]
#defines the bot
chatbot = ChatBot(
    'Alpha',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.40
        }
    ],
    #this adds small functions processing to clean remaining problematic words 
    #that could break the system
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace', #cleans any wrong spacing with regex
        'chatterbot.preprocessors.unescape_html',   #Convert escaped html characters into unescaped html characters
        'chatterbot.preprocessors.convert_to_ascii',
    ]
)

#set params for TRAINING THE BOT
trainer=ChatterBotCorpusTrainer(chatbot)
def trainchatbot(trainer): #works in tandem with bootnoise.startupnoise1()
    trainer.train(
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations",
        "chatterbot.corpus.english.ai"
    )
    trainer=ListTrainer(chatbot)
    trainer.train(conversation)
    trainer.train(conversation1)
    trainer.train(conversation2)
    trainer.train(conversation3)
    trainer.train(conversation4)
    trainer.train(conversation5)
    trainer.train(conversation6)
    trainer.train(conversation7)
    trainer.train(conversation8)
    trainer.train(conversation9)


def alpha_main():
    user_name=checkuserdata()[0]
    user_gender=checkuserdata()[2]
    random_functions = random.randint(1,2)
    if int(random_functions) == 1:
        wishMe(user_gender)
    elif int(random_functions) == 2:
        wishme2(user_name)
    while True:
        query = str(query)
        query=listen.lower()
        if query.startswith("alpha"):
            #listen 
            print("listen")
            for x in extrawords:
                if x in query:
                    query= query.replace(x,"")
                else:
                    continue
            #direct function calls
            if query.startswith("wikipedia"):
                query=query.replace("wikipedia","")
                search_wiki(query)
            elif query.startswith("wiki"):
                query=query.replace("wiki","")
                search_wiki(query)
            elif query.startswith("dictionary"): #need to scan: allow one word only
                query=query.replace("dictionary","")
                search_meaning(query)
            elif query.startswith("meaning"):
                query=query.replace("meaning","")
                search_meaning(query)

            #system actions
            elif query.startswith("system"):
                print("System actions")
                if "ram" in query:
                    checkram()
                elif "cpu" in query:
                    checkcpu()
                elif "battery" in query:
                    checkbattery()
                elif "stat"  in query:
                    systemstats()
                elif "shut down" in query:
                    shutdown_s()
                elif "kill" in query:
                    kill()
                elif "flush DNS":
                    flushdns()
                elif "location":
                    my_location()
                else:
                    speak("Unknown command for system")
            
            #humane query
            elif query.startswith('what'):
                query=query.replace('what','')
            

            elif query.startswith('where'):
                query=query.repalce('where','')

            elif query.startswith('when'):
                query=query.replace("when","")
            
            elif query.startswith('how'):
                query=query.replace("how",'')

            
            else:
                print("AI response")

            

            #cannot identify, dont understand or give AI response
        else:    
            #ignore 
            print("ignore")
        
        