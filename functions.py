def reporterror(errorr, suggest):
    print(errorr + suggest)
#import modules
import discord
from discord import channel
from discord.ext import commands
from sys import excepthook
import pyttsx3
import os
import wikipedia
import time
import os
import os.path
from os import error, path
import eel
from datetime import date
import speech_recognition as sr
import datetime
import datetime
import os
import time
import random
import csv
from pygame import mixer
import pandas as pd
import numpy as np
from threading import Thread
import platform
import discord
import psutil
from win10toast import ToastNotifier
from bs4 import BeautifulSoup as bs
import requests
import time
import requests
from bs4 import BeautifulSoup
import sys
import operator
import json
from response import *
from functions import *
#syntax alarm(hour, minute)
try:
    import webbrowser
except ImportError:
    reporterror("Module webbrowser not found", "Legit, fix your damn pc")
try:
    from googlesearch import search
except ImportError:
    reporterror("module google not found", "Check pip installation")

#load user data functions
print("Checking user data...")
if path.isfile('data.json') == False:
    reporterror("User.txt not found", "Run usersettings.exe please")
    os.startfile("hmm.vbs")
    time.sleep(30)
    exit()
#user data reconfirmation in backend
print("Loading user data.")
with open("data.json", "r") as read_file:
    userdata = json.load(read_file) 
    main_data=userdata["main_user_data"]
    user_name=main_data["username"]
    usercity=main_data["usercity"]
    user_gender=main_data["usergender"]
    user_dob=main_data["userdob"]
    user_email=main_data["useremail"]
    user_email_password=main_data["useremailpass"]
    user_species=main_data["userspecies"]
    user_bloodtype=main_data["userbloodtype"]
    user_skincolor=main_data["userskincolor"]
    user_ethnicity=main_data["userethnicity"]
    user_religion=main_data["userreligion"]
    user_weight=main_data["userweight"]
    user_height=main_data["userheight"]
    user_sport=main_data["usersport"]
    user_hobby=main_data["userhobby"]
    user_interest=main_data["userinterest"]
    user_discord=main_data["userpersonaldiscordbottoken"]
    print("Confirming user data")
    print(user_name)
    print(usercity)
    print(user_gender)
    print(user_dob)
    print(user_email)
    print(user_email_password)
    print(user_species)
    print(user_bloodtype)
    print(user_skincolor)
    print(user_ethnicity)
    print("All data confirmed and detected")
# create an object to ToastNotifier class
dataconfirm = ToastNotifier()
dataconfirm.show_toast("Alpha", "User data confirmed", duration = 5, icon_path ="app.ico")

#notify functiion
def notify(title, content, duration):
    dataconfirm = ToastNotifier()
    icon_path="app.ico"
    dataconfirm.show_toast(title, content, duration, icon_path)


#tts
def speak(audio):
    print(audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
#speech recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening>>>")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing: ")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        print(e)
        print("Audio not heard, plesae try again")
        return "None"
    return query

def dictionary(word):
    from bs4 import BeautifulSoup
    word = str(word)
    speak("Pronounced as" + word)
    url = "http://dictionary.cambridge.org/dictionary/british/" + word.lower()
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    word = soup.find("span", {"class": "pos"}).text
    definition = soup.find("span", {"class": "def"}).text
    speak("It is usually used as a " +word)
    speak("It means"+definition)
def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]
def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    file=open("user.txt","r")
    file.readlines
    if "Male" in  user_gender:
        speak("I am Alpha! Sir, Please tell me how may I help you")
        print("I am Alpha")
    else:
        speak("I am Alpha! Madam, please tell me how may I help you.")       
def wishme2():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        speak(  user_name + "What are you planning to do?" )
    
    elif hour>=12 and hour<18:
        speak("Good afternoon, ready to continue work?")
    else:
        speak("Good evening! " +  user_name)
        speak("How is your day?")

def screenshot():
    import pyautogui
    img = pyautogui.screenshot()
    img.save('"C:\Pictures"/screenshot.png')
    speak("Okay, it is now in your Pictures folder")
def covid19():
    country =  usercity
    worldmetersLink = "https://www.worldometers.info/coronavirus/"
    try:
        html_page = requests.get(worldmetersLink)
    except requests.exceptions.RequestException as e: 
        print(e) #ConnectionError
        speak("You have been diconnected from the internet")
        exit()
    search = bs.select("div tbody tr td")
    start = -1
    for i in range(len(search)):
        if search[i].get_text().find(country) !=-1:
            start = i
            break
    data = []
    for i in range(1,8):
        try:
            data += [search[start+i].get_text()]
        except:
            data += [0]
    message = "Total infected: {} cases, New Case: {} cases, Total Deaths: {} cases, New Deaths: {} deaths, Recovred: {} patients, Current active Case: {} cases, Serious Critical: {} people".format(*data)
    if  user_gender=="Male":
        speak("Sir, today's cases are as follow" + message)
    else:
        speak("Madam, today's cases are as follow" +message)
import requests 
from pprint import pprint
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
	return res.json();
def print_weather(result,usercity):
    speak("{}'s temperature is {} degress Celcius ".format(usercity,result['main']['temp']))
    speak("Wind speed is {} meters per second".format(result['wind']['speed']))
	
    speak("The weather looks {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
def weathermain(usercity):
	print()
	try:
	  query='q='+usercity;
	  w_data=weather_data(query);
	  print_weather(w_data, usercity)
	  print()
	except:
	  print('City name not found...')
def sing():
    speak("I do not think you will like it")
def sing2():
    speak("Okay, if you insist. Never gonna give you up, never gonna let you down. Never gonna turn around, and desert you. ")
    time.sleep(1)
    speak("We are really vibing.")
#weathermain(usercity)
def sayhello():
    speak("Hello everyone." +  user_name + "who are these people")
def sayhello2():
    speak( user_name + "I feel awkward.")
def sing():
    speak("I do not think you will like it")
def sing2():
    speak("Okay, if you insist. ")
    time.sleep(1)
    speak("Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you")
def alarm(hour, minute): 
    print(hour)
    print(minute)
    # Verify whether time entered is correct or not.
    def verify_alarm(hour,minute,seconds):
        if((hour>=0 and hour<=23) and (minute>=0 and minute<=59) and (seconds>=0 and seconds<=59)):
            return True
        else:
            return False
def getnews(): 
    # url definition
    url = "https://www.theguardian.com/uk"
    
    # Request
    r1 = requests.get(url)
    r1.status_code

    # We'll save in coverpage the cover page content
    coverpage = r1.content

    # Soup creation
    soup1 = BeautifulSoup(coverpage, 'html5lib')

    # News identification
    coverpage_news = soup1.find_all('h3', class_='fc-item__title')
    len(coverpage_news)
    
    number_of_articles = 5

    # Empty lists for content, links and titles
    news_contents = []
    list_links = []
    list_titles = []

    for n in np.arange(0, number_of_articles):

        # We need to ignore "live" pages since they are not articles
        if "live" in coverpage_news[n].find('a')['href']:  
            continue

        # Getting the link of the article
        link = coverpage_news[n].find('a')['href']
        list_links.append(link)

        # Getting the title
        title = coverpage_news[n].find('a').get_text()
        list_titles.append(title)

        # Reading the content (it is divided in paragraphs)
        article = requests.get(link)
        article_content = article.content
        soup_article = BeautifulSoup(article_content, 'html5lib')
        body = soup_article.find_all('div', class_='content__article-body from-content-api js-article__body')
        x = body[0].find_all('p')

        # Unifying the paragraphs
        list_paragraphs = []
        for p in np.arange(0, len(x)):
            paragraph = x[p].get_text()
            list_paragraphs.append(paragraph)
            final_article = " ".join(list_paragraphs)

        news_contents.append(final_article)

    # df_features
    df_features = pd.DataFrame(
         {'Content': news_contents 
        })

    # df_show_info
    df_show_info = pd.DataFrame(
        {'Article Title': list_titles,
         'Article Link': list_links,
         'Newspaper': 'The Guardian'})    
    print(df_features + df_show_info)
    return (df_features, df_show_info)
