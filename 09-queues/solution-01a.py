q = []

def add():
    q.append(input("serving ticket..."))

def served():
    global q

    if len(q)>0:
        q = q[1:]
    else:
        print("No tickets in queue")

def ui():
    u = ""
    while u != "3":
        u = input("1 to add to queue\n2 to serve next customer\n3 to quit")
        if u == "1":
            add()
        elif u == "2":
            served()
        print(q)

ui()
