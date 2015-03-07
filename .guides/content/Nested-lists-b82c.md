> **Reminder:** nested lists are multi-dimensional arrays where each element can be accessed by multi-index, 
>e.g. `x[r][c]` will give us an element of the two dimensional list at certain row and column.

## Task 1

Open [task-01.py](open_file "04-nested-lists/task-01.py")

Run the program by pressing the 'Run File' button in the top menu.

It should output

```
[['Bobby', '12 Castle Place', 1998, 'm'], ['Norma', '6 Woods Lane', 1998, 'f']]
6 Woods Lane
```

## Task 2

Zipping lists creates nested lists where each row is made up of the first list's first item as column 0, and the second list's first item as column 1.

| John | Eric | Monty | | Cleese | Idle | Pyton |

becomes

| John Cleese | Eric Idle | Monty Python |


Consider this code.

```python
li1 = ["John","Eric","Monty"]

li2 = ["Cleese","Idle","Python"]

li3 = list(zip(li1,li2))

print(li3)
print(li3[1][0], li3[1][1])
```

Which results in

```
[('John', 'Cleese'), ('Eric', 'Idle'), ('Monty', 'Python')]
Eric Idle
```

You can see we merged one-dimensional lists into a 2 dimensional array. We were able to access two elements of this array and print them out as one string.

**Extension activity:** Create 2 lists of 5 major geographic discoveries, where the first list will contain the dates, e.g. 1805, and the second list will contain the description, e.g. The Battle of Trafalgar. 

Write a program that will "zip" these lists into one 5 element list each element of which contains the date and the description, e.g. 1805 The Battle of Trafalgar.
