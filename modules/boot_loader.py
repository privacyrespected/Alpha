from sys import modules
from threading import Thread
from modules.boot_noise import *
from modules.boot_message import *
from modules.boot_checkuserdata import checkuserdata
from modules.sense import notify
import random
def startup():
    user_name=checkuserdata()[0]
    user_gender=checkuserdata()[2]
    random_functions = random.randint(1,2)
    if int(random_functions) == 1:
        wishMe(user_gender)
    elif int(random_functions) == 2:
        wishme2(user_name)
def bootloader(): #only this is meant to be called
    try:
        Thread(target=startupnoise).start()
        Thread(target=startupnoise2).start()
        Thread(target=startup()).start()
    except Exception as e:
        print(e)
        notify("OHNO", e, 90)
