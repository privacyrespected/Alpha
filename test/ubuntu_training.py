import logging
from chatterbot import ChatBot
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Alpha',logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation'])
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "Hi",
    "Hello,i am Alpha, your personal assitant, How can i help you",
    "who are you?",
    "I am Alpha, your personal assitant",
    "Hello",
    "Hi,I am Alpha, your personal assitant, How can I help you",
    "what should i ask you?",
    "there are many things you can ask me",
    "bye"
    "nice to meet you",
    "talk to you later",
    "ok thanks for talking with me.",
    "thank you",
    "its my honour to help you.",
    "who created you?",
    "NuggetCatSoftware",
    "bye",
    "thank you for talking to me,have a nice day.",
    "hello,i am",
    "nice to meet you.",
    "what's up?",
    "nothing much you tell",
    "i am fine, thanks",
    "good to know that",
    "how are you?",
    "i am fine and thinking same for you.",
    "what is your name?",
    "I am Alpha, your personal assistant",
    "ok",
    "that's great to hear",
    "thanks",
    "at your service"
]
trainer = UbuntuCorpusTrainer(chatbot)
trainer.train()
trainer3 = ListTrainer(chatbot)
trainer3.train(conversation)
trainer2 = ChatterBotCorpusTrainer(chatbot)
trainer2.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.ai"
)
# Start by training our bot with the Ubuntu corpus data


# Now let's get a response to a greeting
while True:
    query=input("User: ")
    response = chatbot.get_response(query)
    print("Bot: "+response)
    trainer.export_for_training('./my_export.json')