#this file is for running code from the ipynb because reasons
from nltk import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = ['be', 'is', 'are', 'were', 'was']
for word in words:
    print(lemmatizer.lemmatize(word, pos='v'))