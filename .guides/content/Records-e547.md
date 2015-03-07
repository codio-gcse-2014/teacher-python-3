# Records and multidimensional arrays via nested lists in Python.

A record is a list. A database is a list of records, therefore, it is a list of lists – a nested list. In Python, this is very efficient.

## Task 1

Open [task-01.py](open_file "07-records/task-01.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
Boo Boo from Mexico is a smallest dog in the world!
Lola from USA is a smallest cat in the world!
```

## Task 2

Here is another program making use of record-like structures.
Open [task-02.py](open_file "07-records/task-02.py"), then add more questions and validation for empty input from a user.

```
Enter pupil's nameJo
Quiz 1 result?23
Quiz 2 result?56
Record complete
['Jo', '23', '56']
Enter another pupil?y
Enter pupil's nameJenna
Quiz 1 result?79
Quiz 2 result?67
Record complete
['Jenna', '79', '67']
Enter another pupil?n
Main list
[['Jo', '23', '56'], ['Jenna', '79', '67']]
```
