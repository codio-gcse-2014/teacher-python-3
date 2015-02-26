twoDeeList = []
fread = open("Book1.csv","rt")
tempRow = []

for line in fread:
    #remove space and comma, ie. Two characters from the right
    noNewLineChar = line.strip()[:-2]

    print(noNewLineChar)

    if noNewLineChar[0] != "," and noNewLineChar[0] != "":
        twoDeeList.append(noNewLineChar.split(","))

fread.close()

print("List in raw form")
print(twoDeeList)

print("List in nicer form")

for element in twoDeeList:
    print(" ".join(element))
