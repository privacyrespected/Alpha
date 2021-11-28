from bs4 import BeautifulSoup
import requests
def dictionary(word):

    from bs4 import BeautifulSoup
    word = str(word)

    url = "http://dictionary.cambridge.org/dictionary/british/" + word.lower()
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    wordform = soup.find("span", {"class": "pos"}).text
    definition = soup.find("span", {"class": "def"}).text    
    output=(word+ "a" + wordform+ "means"+ definition)
    return output