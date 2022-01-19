import py_compile
import re
puncuations=[
    "`",
    "~",
    "!",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "+",
    "?",
    ".",
    ","

]

def clean_punctuations(statement):
    print(statement)
    for x in puncuations:
        if x in statement.text:
            statement.text=statement.text.replace(x,"")
        else:
            continue
    return statement