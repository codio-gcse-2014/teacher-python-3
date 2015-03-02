# Task 2
# Press the 'Run File' menu button to execute
# 
Records = []
EnterAnother = ""

while EnterAnother != "n".lower():
    aRecord = []

    # Fill one record with user's input
    pName = input("Enter pupil's name")
    aRecord.append(pName)

    pQuiz1 = input("Quiz 1 result?")
    aRecord.append(pQuiz1)

    pQuiz2 = input("Quiz 2 result?")
    aRecord.append(pQuiz2)

    print("Record complete")
    print(aRecord)

    # copy aRecord into Records
    Records.append(aRecord)

    # ask user to continue data entry
    EnterAnother = input("Enter another pupil?")

print("Main list")
print(Records)
