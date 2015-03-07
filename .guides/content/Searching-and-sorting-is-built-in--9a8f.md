## Task 1

Python allows to sort lists using the built-in sorted function. Note, that the original list is not affected, we get a sorted copy of the original list and that is what being printed. This is similar to an SQL select query that brings us a copy of a table without modifying its data.

Open [task-01.py](open_file "03-searching/task-01.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
1
['Amir', 'Pamela', 'Bob']
['Amir', 'Bob', 'Pamela']
```

## Task 2


We often need to append to lists by asking a user to supply the new values. This program will accomplish just that.

Open [task-02.py](open_file "03-searching/task-02.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
Who joined the team? >> Bobby
['Jill', 'Adam', 'Amir', 'Norah', 'Bobby']
Type <Enter> to add another, or type 'quit' to exit >>
Who joined the team? >> Jessica
['Jill', 'Adam', 'Amir', 'Norah', 'Bobby', 'Jessica']
Type <Enter> to add another, or type 'quit' to exit >> quit
>>>
```

## Task 3

Once we have a good list, we can manipulate it. Here we will randomly pick winners off a list of names. 

We will create a function that generates a random number within the dimensions of our list, then it will remove (pop) an item stored at an index equal to the random number generated, e.g. if the random number was 2, then Amir will be removed. 

However, the "pop" function in Python has a second functionality. As it is removing an item it can copy it to somewhere – in this case, it will be passed out of a function.

This is handy for the games of chance and any game AI.

Open [task-03.py](open_file "03-searching/task-03.py").

Run the program by pressing the 'Run File' button in the top menu.

It should output

```
Third prize Bob, Second prize Anna, ***FIRST PRIZE*** Amir
```
