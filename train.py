# -*- coding: utf-8 -*-
#this file is for testing the machine learning system and pretrain any data so to reduce startup time (might be cap tho)
from chatterbot import ChatBot
from chatdata import * 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

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
            'default_response': 'I am sorry, but I do not understand (time).',
            'maximum_similarity_threshold': 0.40
        }
    ]
)

trainer=ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.ai"
)
trainer=ListTrainer(chatbot)
trainer.train(conversation)
# Get a response to the input text 'How are you?'
while True:
    query=input("Input: ")
    response = chatbot.get_response(query)
    
    conf=int(response.confidence)
    
    if response.confidence >= 0.65:
        response=str(response)
        print("good confidence")
        print("conf: "+ str(conf))
        print(str("output: "+response))
    else:
        response=str(response)
        print("bad confidence")
        print("conf: "+ str(conf))
        print(str("output: "+response))