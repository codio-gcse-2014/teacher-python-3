# Task 1
# Press the 'Run File' menu button to execute
# 
li = list(range(0,10))

def over_five(lx):
    return lx>5

# this takes all x's that fit the criteria specified in a function.
filt_li = [x for x in li if over_five(x)]

print(filt_li)
