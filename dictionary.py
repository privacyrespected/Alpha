from bs4 import BeautifulSoup
import requests
def dictionary(word):
    word = str(word)
    url = "http://dictionary.cambridge.org/dictionary/british/" + word.lower()
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    word = soup.find("span", {"class": "pos"}).text
    definition = soup.find("span", {"class": "def"}).text
    print(word)
    print(definition)