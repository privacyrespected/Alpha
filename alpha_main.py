#Import modules
from winreg import QueryValue
from modules.display import slowprint
from modules.display import ascii
from modules.bootloader import checkuserdata, startup_main
from modules.sense import listen, speak
from corpus.extrawords import *
####################################
#INTRO
results=ascii("ALPHA V4.0")
print(results)
slowprint("Designed by PrivacyRespected in the United Kingdom")
######################################################################################
#GREET 
startup_main()
#######################################################################################
