## Task 1

A speleologist relies on a Python program installed on his handheld device to keep track of all the special features, e.g. "sharp drop", etc. 

Write a program that will allow the user, as he goes through the cave, to store a list of features or notes to self in reverse chronological order. 
E.g. 
- "sharp drop", 
- "low ceiling", 
- "3 stalagmites",
- "long walk",
- "cave entrance". 

Then as he goes back and comes across the feature, he can delete it off the list to avoid confusion.

Open [play.py](open_file "10-stacks/play.py").

Implement this program.

## Solution

You can find the solution in [solution-01.py](open_file "10-stacks/solution-01.py").

The expected output is,
```
>>>
1 to add a feature
2 if you see the feature
3 to quit1
What do you see?Sharp drop
['sharp drop', 'low ceiling', '3 stalagmites', 'long walk', 'cave entrance', 'Sharp drop']
1 to add a feature
2 if you see the feature
3 to quit2
['sharp drop', 'low ceiling', '3 stalagmites', 'long walk', 'cave entrance']
1 to add a feature
2 if you see the feature
3 to quit2
['sharp drop', 'low ceiling', '3 stalagmites', 'long walk']
1 to add a feature
2 if you see the feature
3 to quit2
['sharp drop', 'low ceiling', '3 stalagmites']
1 to add a feature
2 if you see the feature
3 to quit2
['sharp drop', 'low ceiling']
1 to add a feature
2 if you see the feature
3 to quit2
['sharp drop']
1 to add a feature
2 if you see the feature
3 to quit2
[]
1 to add a feature
2 if you see the feature
3 to quit2
You should be back at the cave entrance ;)
[]
1 to add a feature
2 if you see the feature
3 to quit3
[]
```
