from urllib.parse import quote_from_bytes


list=[
    "a",
    "b",
    "c",
    "d"
]
while True:
    word =input(">> ")
    for check in list:
        if check in word:
            print("The word is in the list!")
            word=word.replace(check,"")
            print(word)
            
        else:
            continue
    print("Done")
        

import geocoder

g = geocoder.ip('me')
print(g.latlng)