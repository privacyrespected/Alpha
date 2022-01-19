#this file is used to group ALL parts of the program into one file
#Compile only this file as all others are just functions and only this file can call it
print("Alpha V3")
print("nuggetcatsoftware@gmail.com")

#import modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from customcorpus import *
from chatterbot import preprocessors
#this line implements the custom chatterbot preprocessors for extra word filter
from preprocessors import clean_words
from modules.sense import *
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
        'preprocessors.clean_words.clean_words',
        'preprocessors,clean_puncuations,clean_puncuations'
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

