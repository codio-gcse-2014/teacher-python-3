a = [] # create empty list

# add things to it (first element is at zero position):
a.append(2)

# test if it worked - see the whole list
print(a)

#add another
a.append(45)

# test and show the whole list
print(a)

# overwrite first item which originally was 2 with 11
a[0] = 11

# test
print(a)

# sometimes, we don't wan't to put new items at the end
# here we put it in a specific position - the first one [0]
a.insert(0,10)
a.append([33,44])
a.extend([33,44])

print (a)
