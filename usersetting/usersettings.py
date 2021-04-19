import eel
import time
import os
from datetime import date
import datetime
import eel
def reporterror(errorr, suggest):
    print(errorr)
    today = date.today()
    errordate = today.strftime("%d/%m/%Y")
    now = datetime.now()
    errortime = now.strftime("%H:%M:%S")
    f=open("errorlog.txt", "w")
    f.write("ERROR")
    f.write("\n")
    f.write("Error date: "+errordate)
    f.write("\n")
    f.write("Error time: "+errortime)
    f.write("\n")
    f.write("Error: ")
    f.write("\n")
    f.write(errorr)
    f.write("\n")
    f.write("Suggestions: ")
    f.write("\n")
    f.write(suggest)
    f.close()
def error():
    print("bruh")
    os.startfile("error.vbs")

eel.init("settingweb")

@eel.expose
def usersettingwrite(username, usercity, user_gender, userdob, useremail, useremailpass):
    try:
        print("Name: " + username)
        print("Usercity: " + usercity)
        print("usergender: " + user_gender)
        print("userdob: " + userdob)
        print("useremail: " + useremail)
        print("useremailpass: " + useremailpass)
        if username=="":
            error()
        if usercity=="":
            error()
        if user_gender=="":
            error()
        if userdob=="":
            error()
        if useremail=="":
            error()
        if useremailpass=="":
            error()
        else:
            time.sleep(1)
            print("Creating a new user profile")
            f= open("user.txt","w+")
            f.write("\n")
            f.write(username)
            f.write("\n")
            f.write(usercity)
            f.write("\n")
            f.write(user_gender)
            f.write("\n")
            f.write(userdob)
            f.write("\n")
            f.write(useremail)
            f.write("\n")
            f.write(useremailpass)
            time.sleep(1)
            f.close()
    except Exception as e:
        print(e)
        reporterror(e, "Open issue oon github")


eel.start("homesetting.html",cmdline_args=['--start-fullscreen'], port=1111)
