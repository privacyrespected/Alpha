#SAMPLE FOR PREPROCESSORS
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
