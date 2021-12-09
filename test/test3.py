import wikipedia
while True:
    try:
        query=input("Wikipedia summary: ")
        output=wikipedia.search(query,results=3, suggestion=True)
        output2=wikipedia.summary(query,sentences=2)
        print(output)
        print(output2)
    except Exception as e:
        print(e)
        continue