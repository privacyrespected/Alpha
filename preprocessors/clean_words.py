import re
#this file imports the regex and cleans any extra words that is preventing the processing of this program

#this is the list of the words that will be removed during processing
#it will be rmemoved at the start so be aware that you do not process any of these words

extrawords=[
    "please",
    "would you mind",
    "do you mind",
    "tell me",
    "let me know",
    "you",
    "alpha",
    "telling me",
    "can you"
]
def clean_words(statement):
    for x in extrawords:
        if x in statement.text:
            statement.text=statement.text.replace(x,"")
        else:
            continue
    return statement
