list = [
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
    "hello,i am xxx",
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
    "at your service",
    "fuck",
    "You seem angry, is there something I can help",
    "nigger",
    "Please refrain from racial slurs, we are all created equal",
    "you are great",
    "thanks, your opinion is valuable to my growth"
]
while True:
    query=input("test to debug: ")
    for cont in list:
        if cont in query:
            print("Positive")
        else:
            print("negative")