from alpha_main import wishMe
from alpha_main import wishme2
from alpha_main import alphamain
from alpha_main import alpha_frontend
from threading import Thread
if __name__ == "__main__":
    print("started")
    import random
    print(random.randint(1,2))
    random_functions = random.randint(1,2)
    if int(random_functions) == 1:
        wishMe()
    elif int(random_functions) == 2:
        wishme2()
    Thread(target=alphamain).start()
    Thread(target=alpha_frontend).start()
