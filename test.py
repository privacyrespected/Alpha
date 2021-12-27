G = None

def foo():
    global G
    if G is None:
        G = 1
        print(str(G))
    print(str(G))
foo()