from chatterbot import ChatBot, conversation
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot=ChatBot("BOT", logic_adapters=[
    'chatterbot.logic.BestMatch',
    'chatterbot.logic.TimeLogicAdapter',
    'chatterbot.logic.MathematicalEvaluation'
])
conversation1=[
    "hi",
    "hello there",
    "what can you do",
    "i can play gta on nokia"
]
trainer=ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.ai"
)
trainer=ListTrainer(chatbot)
trainer.train(conversation1)
while True:
    query=input("Input to debug: ")
    response=chatbot.get_response(query)
    print(response)
    trainer.export_for_training('./testdata.json')
