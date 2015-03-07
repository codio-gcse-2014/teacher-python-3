## Task 1

"Enumerating" through a list – that means printing out not just the items but their positions, like so:

```python
a = ["Bob","Pela","John"]

for index,item in enumerate(a):
    print("{} is at position {}".format(item,index))
```

The result:

```
Bob is at position 0
Pela is at position 1
John is at position 2
```

## Task 2

Comparing lists:

Python is able to evaluate if a statement is true or false. For example, `5 > 3` will return `True`, and `4 == (2 * 2)` will also return `True`, while `3 * 3 == 3 ** 3` will return `False` (`3 ** 3` means `3` to the power of `3`).

Open [task-02.py](open_file "02-list-operations/task-02.py")

Run the program by pressing the 'Run File' button in the top menu.

It should output

```
False
```

## Task 3


Open [task-03.py](open_file "02-list-operations/task-03.py").

Run the program by pressing the 'Run File' button in the top menu.

It should output

```
['Bob', 'Pamela', 'Amir']
Bob
Pamela
Amir
Bobdelimiter Pameladelimiter Amir
```

**Extension:** modify the program above, so that the word "delimiter" doesn't run into their names.

## Task 4

Performing calculations on list items en masse:

Open [task-04.py](open_file "02-list-operations/task-04.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
0
2
4
6
8
10
12
14
16
18
```

## Task 5

Open [task-05.py](open_file "02-list-operations/task-05.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
All list items must be strings to join
```

## Task 6

To make "join" work on the list items, we need to individually convert them to strings. Our knowledge of list comprehension (running one-line loops through lists) will come in handy.

Open [task-06.py](open_file "02-list-operations/task-06.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
```
