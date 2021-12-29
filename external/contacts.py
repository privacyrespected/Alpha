import sqlite3
dbase = sqlite3.connect('contacts.db')
dbase.execute('create table if not exists' +
                ' contact(name text,gender text,status text,personality text,dob text,phonenumber text,nationality text)')

cur=dbase.cursor()
def contact_check(query_name):
    cur.execute(F'select name from contact where name="{query_name}"')
    obj = cur.fetchall()
    if obj:
        return True
    else:
        return False
def contact_delete(query_name):
    query_name=query_name.title()
    if contact_check(query_name):
        cur.execute(f"delete from contact where name='{query_name}'")
    else:
        print(f"No contact exit for name: {query_name}")
        return "404 not found"
def contact_addnew(query_name,query_gender, query_status, query_personality, query_dob, query_phonenumber,query_email,query_nationality):
    query_name=query_name.title()
    cur.execute('insert into contact values(?,?)', 
    (f'{query_name}', f'{query_gender}',f'{query_status}',f'{query_personality}',f'{query_dob}',f'{query_phonenumber}',f'{query_nationality}',f'{query_email}'))
    print("new contact added")
    dbase.commit()
#adds new  contact