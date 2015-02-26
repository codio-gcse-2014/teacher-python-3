# source data - often in the form of a dictionary
records = {
    "I23": [
        "Ingwar",
        23,
        False
    ],
    "D13": [
        "Denis",
        13,
        True
    ],
    "A3": [
        "Amir",
        35,
        False
    ]
}

index_list = list(records.keys())

# open a file in a write mode
f = open("csv.txt","wt")

for r in index_list:
    # add commas to separate values, iterate through keys
    # in our dictionary.
    f.write(r+",")

# every key has a few fields related to it, so we
# need a nested loop to write multiple fields per key.
for field in records[r]:
    print(field)

f.write(str(field)+", ")

#insert a new line character starting a new row
f.write("\n")

# files open for writing must be explicitly closed to commit the changes.
f.close()

import os

# this will launch Notepad with our file (this only works on Windows)
os.system('notepad.exe ' + "csv.txt")
