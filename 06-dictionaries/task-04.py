# Task 4
# Press the 'Run File' menu button to execute
# 
myD = {
    "Mike": "brother-in-law",
    "Bob": "plumber",
    "Spiderman": "superhero"
}

# print raw form dictionary
print(myD)

# print raw form dictionary - items which include keys and values
print(myD.items())

# print first item
print(myD["Mike"])

# more user-friendly
print("{} is my {}".format("Bob", myD["Bob"]))

# print raw form dictionary - just the keys
print(myD.keys())

#print raw form dictionary - just the values
print(myD.values())
