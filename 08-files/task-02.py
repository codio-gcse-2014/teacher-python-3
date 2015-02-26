listPredictions =  []
listRomantic = []

def readPredictions():
    global listPredictions

    # read the file and load its contents into list1
    f = open("predictions.txt", "rt")
    fileContents = f.read()
    listPredictions = fileContents.split('\n')
    # print(listPredictions)

def readRomantic():
    global listRomantic

    # read the file and load its contents into list1
    f = open("romantic.txt", "rt")
    fileContents = f.read()
    listRomantic = fileContents.split('\n')
    # print(listRomantic)

def getHoroscope():
    print("Get your reading! Press \n1 for Capricorn\n2 for Aries\n3 for Taurus\n4 for Libra")

    choice = int(input(">> "))
    showPrediction(choice)

def showPrediction(zodiacNum):
    try:
        daily = listPredictions[zodiacNum]+". "+listRomantic[zodiacNum]+".\n"
    except:
        print("Error... Feature not implemented, yet.")
    else:
        print(daily)

saveUpdated(daily)

def saveUpdated(pred2append):
    # print("Saving...",pred2append)
    # save my changed list into the same file
    # overwriting its contents

    f = open("history.txt", "a")
    f.write(pred2append)
    f.close()

def mainProgram():

    readPredictions()
    readRomantic()

    continueOK = ""

    while continueOK! = "n":
        getHoroscope()
        continueOK = input("Another horoscope?, y/n")

    print("Peace, out!")

mainProgram()
