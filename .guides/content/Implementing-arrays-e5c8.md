First, we will look at simple lists where items are indexed by their numeric position, e.g. `my_list[0]` is the first element of that array. Then, we will look at a special kind of arrays, known as "associative arrays" or "dictionaries" where we access the elements not by their numeric position in the list but by an associated key, e.g. `my_dict["CUST1202"]` which will pull up an item associated with the key `"CUST1202"`.

## Task 1

Open [task-01.py](open_file "01-implementing/task-01.py") 

Run the program by pressing the 'Run File' button in the top menu.

It should output

```bash
3
Jack is going
```

## Task 2

Next, implement this program that shows two ways of adding to a list. Append adds an item to the last position (first empty). Appending a list to a list, creates a nested list – Python's answer to traditional arrays. Extend also adds items to the end of the list but if the item being added is also a list, it will "flatten" it – extract all of its elements and add them automatically.

Open [task-02.py](open_file "01-implementing/task-02.py").

Run the program by pressing the 'Run File' button in the top menu.

It should output

```
[2]
[2, 45]
[11, 45]
[10, 11, 45, [33, 44], 33, 44]
```

## Task 3

Deleting from lists is done in three ways:

1. Delete from a specified position – `my_list.pop(position)`. Has the added bonus of returning the value being removed (as you sometimes wouldn't know what was the value stored in that position, so you can do print(`my\list.pop(position)` ).
2. Delete a specific value (only deletes the first instance, needs to run repeatedly to remove multiple occurances) – `my_list.remove(value)`
3. List slicing `my_list = my_list[2:4]` – this copies the smaller "slice" between the third `(2)` to 4th element over the original list.

## Task 4a

Add the following lines to the program above:

```python
a.pop(1)
a.remove(10)
```

Let's compare the list contents before and after these two run:

```
[10, 11, 45, [33, 44], 33, 44]
```
```
[45, [33, 44], 33, 44]
```

As you can see, gone is 11 from position 1 (second position in a zero-base list), then 10 from the first position is gone, too.

## Task 4b

If you comment out the two new lines and insert this:

```python
print(a[2:])
```

That should accomplish the same result in the printout and still keep the list intact. If you wanted to delete the two first values permanently, you would type:

```python
a = a[2:]
```

Notice, how despite having the same effect, these three ways of removing items will be best for different applications.
