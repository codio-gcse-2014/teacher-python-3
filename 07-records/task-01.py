# Task 1
# Press the 'Run File' menu button to execute
# 
# create a record structure with fields
class Record():
    who=""
    age=0
    when=""
    what=""
    where=""

# create an empty list to hold future records
Records = []

# declare a particular record and fill in the info

smallestDog = Record()
smallestDog.who = "Boo Boo"
smallestDog.age = 10
smallestDog.what = "smallest dog"
smallestDog.where = "Mexico"

# add this record to the list
Records.append(smallestDog)

# same but for a different record
smallestCat = Record()
smallestCat.who = "Lola"
smallestCat.age = 3
smallestCat.what = "smallest cat"
smallestCat.where = "USA"

Records.append(smallestCat)

# use an "each" loop to run through all records

for each in Records:
    print(each.who + " from " + each.where + " is a " + each.what + " in the world!")
