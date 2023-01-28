#this function is to display words on the terminal
#cannot be observed on front end
import sys
import time
import pyfiglet
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./1000)
def ascii(input):
    result= pyfiglet.figlet_format(input)
    return result
