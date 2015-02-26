s = ["sharp drop", "low ceiling", "3 stalagmites","long walk", "cave entrance"]

def add():
    s.append(input("What do you see?"))

def went_through():
    global s

    if len(s) > 0:
        s = s[:-1]
    else:
        print("You should be back at the cave entrance ;)")

def ui():
    u = ""
    while u != "3":
        u = input("1 to add a feature\n2 if you see the feature\n3 to quit")

        if u == "1":
            add()
        elif u == "2":
            went_through()
        print(s)

ui()
