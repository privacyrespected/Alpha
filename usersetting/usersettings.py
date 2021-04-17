import eel
import time
import os
import eel

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


eel.start("homesetting.html",cmdline_args=['--start-fullscreen'], port=1111)
