# Task 2
# Press the 'Run File' menu button to execute
# 
Contestants = ["Jill","Adam","Amir","Norah"]

def add_new():
    uContinue = ""

    while uContinue != "quit":
        newContestant = input("Who joined the team? >> ")

        # adds to the end
        Contestants.append(newContestant)

        print(Contestants)

        uContinue = input("Type <Enter> to add another, or type 'quit' to exit >> ")

add_new()
