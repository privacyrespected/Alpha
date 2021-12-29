import re

def addperson(query):
    print("ok")
    if "name" in query:
        print("name found")
        print(query)
        query_name=re.search("^name (\w+)",query)
    print(query_name) #shd just output gabs
    x=query_name.group(1)
    print(x)
    #<_sre.SRE_Match object; span=(0, 9), match='name gabs'>
addperson("name gabs matthews")

#intend to output the name as gabs