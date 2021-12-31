from response import *
import re 
query="add person name gabs gender male status hostile personality nice nationality afghan"
def addperson(query):
    #remove extra words here
    for x in be:
        if x in query:
            query=re.sub(x,"",query)
        else:
            continue
    ###all extra words removed here
    if "name" in query:
        query_name=re.search("^name (\w+)",query)
        query_name=query_name.group(1)
    if "gender" in query:
        query_gender=re.search("^gender (\w+)",query)
        query_gender=query_gender.group(1)
    if "status" in query:
        query_status=re.search("^status (\w+)",query)
        query_status=query_status.group(1)
    if "personality" in query:
        query_personality=re.search("^personality (\w+)",query)
        query_personality=query_personality.group(1)
    if "nationality" in query:
        query_nationality=re.search("^nationality (\W+)",query)
        query_nationality=query_nationality.group(1)
    query_dob="Null"
    query_phonenumber="Null"
    query_email="Null"  
    print(query_name,query_gender,query_dob,query_status,query_personality,query_phonenumber,query_nationality)
addperson(query)
