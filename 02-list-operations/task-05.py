# Task 5
# Press the 'Run File' menu button to execute
# 
# this will not work for numeric items, as the Python join
# function only works on strings.

# use of error catching which prevents a nasty crash of this program
try:
    # try "\t" instead of the "-"
    print(" - ".join(a))
except:
    print("All list items must be strings to join")
