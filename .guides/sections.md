---
title: "Arrays, Queues and Stacks"
files:
  - action: close
    path: "#tabs"
layout: 3-cell-tree

---
Arrays, queues and stacks are the three most popular data structures in computer science. All of them store items of a similar nature to be processed in a similar way. These data structures lend themselves well to iteration (looping) and automation, as well as restricting input and output values, which assists validation.

The differences between them are in the level of access. Arrays allow access to all of their elements in any order. Their size is usually fixed in advance (but can be resized at runtime) and arrays are slow and take up more memory – the price to pay for the convenience of full access. A mechanical analogy would be that of a revolver – by spinning the drum, any individual bullet can be "accessed" and the bullets are clearly visible all at once. Similarly, any array element can be overwritten, deleted, copied, etc.

Queues differ from arrays as only two end items, one at the "head", the other at the "tail" are accessible to the program. We "feed" (push) items into the queue on one end, and read/process items (pop) from another end. This saves memory and speeds up the process as only two memory locations need to be open to the rest of the program. The downsides include having to go through the whole queue before a newly-added element can be processed. To continue with our firearms analogy, queue would be like a belt-driven machine gun from the WWI.

Stacks are even more restricted. Only one "end" is accessible to the program, resulting in Last-in-First-Out order of processing. The analogy would be a pistol magazine, where the first bullet loaded will be the last to come out. Stacks are very fast and are used extensively in the CPU.

I wasn't sure about the military terminology here – is it appropriate? It works really well in my current all-boys school.

---
title: Implementing arrays
files:
  - action: close
    path: "#tabs"
layout: ""
step: 01-implementing

---
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

---
title: More useful list operations
files:
  - action: close
    path: "#tabs"
layout: ""
step: 02-list-operations

---
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

---
title: "Searching and sorting is built in!"
files:
  - action: close
    path: "#tabs"
layout: ""
step: 03-searching

---
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

---
title: Nested lists
files:
  - action: close
    path: "#tabs"
layout: ""
step: 04-nested-lists

---
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

---
title: Applying filters to lists
files:
  - action: close
    path: "#tabs"
layout: ""
step: 05-filters

---
The ability to filter lists is very important. Consider a program that is creating a prefect rota. From the list of potential prefects, the program will have to exclude all who are already engaged at a particular time slot, leaving the list of possible candidates.

## Task 1

The following code will take the just-in-time created list of number 0-9 and filter it to only those over 5 using an appropriately called function:

Open [task-01.py](open_file "05-filters/task-01.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
[6, 7, 8, 9]
```

## Task 2

There is more than one way to filter lists and different people end up preferring different types. Replace the line

```python
filt_li = [x for x in li if over_five(x)]
```

with

```python
filt_li = list(filter(over_five,li))
```

We are now making use of the built-in Python function to filter lists. However, this function is being depreciated (its use is discouraged), so make sure you know the other methods, as well.


## Task 3

Now replace the line with this:

```python
filt_li = [x for x in li if x>5]
```
Here, we actually simplified our code, instead of a function which is more flexible and efficient, we are checking the condition (over 5) in the filtering statement itself. If the first two methods were too complicated, this is the one to use.

You should see no difference in output, they are all equivalent. Can you comment on their readability and easy of understanding – which option do you like more?

Read what Python's inventor has to say about this:

[http://www.artima.com/weblogs/viewpost.jsp?thread=98196](http://www.artima.com/weblogs/viewpost.jsp?thread=98196).

There is another commonly used list function called `map`. It runs a specified function on every list item.

## Task 4


Replace the line

```python
filt_li = [x for x in li if over_five(x)]
```

with

```python
filt_li = list(map(over_five,li))
```
The output is then,

```
[False, False, False, False, False, False, True, True, True, True]
```

What did the mapping do?

It replaced the list item with the value of the function in which that list item was an input.

## Task 5

It is not very useful with our `over_five` function, but consider this code:

```python
li=list(range(0,10))

def doubler(lx):
    return lx*2

filt_li=list(map(doubler,li))

print(filt_li)
```

Which would output,

```
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

It doubled all the values, sending every item through the function where it got transformed.

## Task 6


You would get exactly same result by using list comprehension, replace the line

```python
filt_li = list(map(doubler,li))
```

with

```python
filt_li = [doubler(x) for x in li]
```

The output should be exactly same.

Mapping can be quite powerful when you have a long list of items and you need to apply some sort of a transformation to each item (or perhaps, only to the items that match a criteria). 

For example, consider a store that buys items off a wholesaler, adds 30% margin to the cost and then prints out the price tags. In a list of: broccoli, £1.00; milk £1.20; bananas £0.60, we would like to multiply all quantities by 1.3.

It is, of course, possible to do this with a loop, but Python here provides are more efficient and easier to read way of accomplishing the same thing.

---
title: Dictionaries (Associative arrays)
files:
  - action: close
    path: "#tabs"
layout: ""
step: 06-dictionaries

---
Created using curly braces rather than square brackets we use for regular lists. 

There is no numeric indexing, just associations. 

Dictionaries are special lists of pairs that are great for lookups, e.g. English word for a French word, page number and the topic on that page. 

We can say, that a dictionary is like a 2-column list, where the first column must be unique (just like primary key in database entities) and is called … a key. The second column is called a value. Dictionaries don't use indices, so you can't say `dictionary[2]`, instead, to get a particular value, we look it up by its associated key, e.g. `dictionary["1805"]` will possibly return "The Battle of Trafalgar". They are often used in encryption/decryption, as each letter of a text needs to be replaced by its encrypted/decrypted value.

It is fairly easy to see why they are called dictionaries.

## Task 1

Here is a dictionary to an imaginary language:

```python
d_e = {
    "milk": "moo",
    "I": "Me",
    "want": "tu-tu"
}
```

Let's explore the features of dictionaries:

We can extract parts of the dictionary. `Dictionary.items()` will return all pairs stored in the dictionary. `Dictionary.keys()` will return the first column, while `Dictionary.values()` will return the second column.

Open [task-01.py](open_file "06-dictionaries/task-01.py").

Run the program by pressing the 'Run File' button in the top menu.

It should output

```
moo
dict_items([('I', 'Me'), ('milk', 'moo'), ('want', 'tu-tu')])
dict_keys(['I', 'milk', 'want'])
dict_values(['Me', 'moo', 'tu-tu'])
```

This will not work:

```python
# this will not work:

# remember, dictionaries don't use indices like 1
print (d_e.items(1))
print (d_e.keys(1))
print (d_e.values(1))
```

But this will (we convert dictionary items into regular list items):

By putting the word "list" in front of a part of a dictionary, we can convert it to a list

```python
items_list = list(d_e.items())
print(items_list[1])

keys_list = list(d_e.keys())
print(keys_list[1])

values_list = list(d_e.values())
print (values_list[1])
```

outputs,

```
('milk', 'moo')
milk
moo
>>>
```

## Task 2

Open [task-02.py](open_file "06-dictionaries/task-02.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
('want', 'tu-tu')
('milk', 'moo')
('I', 'Me')
want tu-tu
milk moo
I Me

```

## Task 3

Open [task-03.py](open_file "06-dictionaries/task-03.py").

Run the program by pressing the 'Run File' button in the top menu.

It should output

```
I
want
milk!
M e  t u - t u  m i l k !
```

## Task 4

Another dictionary exercise to explore different parts of a dictionary – keys and values separately.

Open [task-04.py](open_file "06-dictionaries/task-04.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
{'Mike': 'brother-in-law', 'Spiderman': 'superhero', 'Bob': 'plumber'}
dict_items([('Mike', 'brother-in-law'), ('Spiderman', 'superhero'), ('Bob', 'plumber')])
brother-in-law
Bob is my plumber
dict_keys(['Mike', 'Spiderman', 'Bob'])
dict_values(['brother-in-law','superhero','plumber'])
```

---
title: Records
files:
  - action: close
    path: "#tabs"
layout: ""
step: 07-records

---
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

---
title: File reading and writing
files:
  - action: close
    path: "#tabs"
layout: ""
step: 08-files

---
## Task 1

Spreadsheets are very important tools in today's office. They are two dimensional lists (sometimes, three dimensional if you count the ability to link cells of different sheets in a workbook. 

Flat file databases that you learn in the database section of the syllabus are also spreadsheets. While there are different packages that can show and allow editing of a spreadsheets, there is one common format that is used to exchange data between different spreadsheet packages. It is called CSV for "comma separated values". 

Below, you see a screenshot of one such a file. On each row, columns are separated by commas (hence, comma-separated), while the new line character separates the rows. This skills is building on GCSE list handling, as some of the tasks come with data stored in the CSV form.

![CSV File](.guides/img/csv.png)


First, in your spreadsheet package of choice, input the data shown in a screenshot above and call it Book1.csv. You can then open it in a Notepad or similar text editor to confirm that commas have been inserted. Then open [task-01.py](open_file "08-files/task-01.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
Bobby,12 Cobblestone,12/12/2001
Toby,April Cottage,12/02/2001
List in raw form
[['Bobby', '12 Cobblestone', '12/12/2001'], ['Toby', 'April Cottage', '12/02/2001']]
List in nicer form
Bobby 12 Cobblestone 12/12/2001
Toby April Cottage 12/02/2001
```

This program opened the file in a read only mode (rt), reads the file line by line, removes the trailing commas at the end of every line.

Extension: implement the solution above without removing the two right-most characters. What is the difference in output?

## Task 2

To go beyond GCSE, we need to learn how to work with multiple files at once. 

Relational databases are an expectation at A level, which means that a program needs to read multiple CSV files (this skill is later transferrable to SQL, which is also required at A level). The program also needs to combine (join) data from different tables matching by their relationships between primary and foreign keys.

This is a horoscope program. It uses global lists, functions and subs, imperative structure with main(), error trapping with try/else, as well as reading from two CSV files and writing to a text file - reading data into respective lists from serial files and writing the predictions to the third serial file:

Open [task-02.py](open_file "08-files/task-02.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
Get your reading! Press
1 for Capricorn
2 for Aries
3 for Taurus
4 for Libra
>> 1
Milkman is your enemy. You have a secret admirer.
Another horoscope?, y/nn
Peace, out!
```

## Task 3

Writing a dictionary to a flat file database in a csv file.
![CSV Example](.guides/img/csv1.png)

Open [task-03.py](open_file "08-files/task-03.py").

Implement a program that can read a CSV file that looks like the screenshot above (Create a new file in your 08-files directory named `csv.csv` - right click the folder and select 'New File').

## Task 4

This program will save a dictionary to a txt file. If we change the file extension to ".csv" from ".txt", we can open this file with a spreadsheet program. Notice, how for convenience, we used Python's ability to run other programs and open files in them – we are launching Notepad with the file we created to save us searching for it.

Open [task-04.py](open_file "08-files/task-04.py").

Run the program by pressing the 'Run File' button in the top menu, and supply comments where needed.

It should output

```
Amir
35
False
Ingwar
23
False
Denis
13
True
```

---
title: Implementing queues
files:
  - action: close
    path: "#tabs"
layout: ""
step: 09-queues

---
We will show a simple way of programming queues through shallow copying a list to itself apart from its first element. If you remember, list slicing allows us to access a sub-list.

The general syntax is:

```python
my_list[beg:end]
```

Since Python lists start from zero, we can get all items but the first like so:

```python
my_list[1:]
```

It is not very efficient with memory, so for industrial-strength applications, Python comes with a special Queue module that you can import and it will give you access to memory efficient features of Queues and Stacks. ( [http://docs.python.org/3.3/library/queue.html](http://docs.python.org/3.3/library/queue.html))

## Task 1

Imagine a screen in a store that shows a currently served customer service ticket on a big screen, as customers tear off a number ticket off a roll at the entrance. A store clerk has an access to a computer where a program allows him/her to enter tickets as they are taken by customers. Tickets registered are entered into the first-come first-served queue. The same clerk then keeps track of the tickets served and removes the processed tickets from the queue. 

The program has a menu with 3 options: 
-  add a ticket; 
-  serve a ticket; 
-  quit. 

Open [play.py](open_file "09-queues/play.py").

Implement this program.

## Solution

You can find the solution in [solution-01a.py](open_file "09-queues/solution-01a.py").

The expected output is,
```
>>>
1 to add to queue
2 to serve next customer
3 to quit1
serving ticket...123
['123']
1 to add to queue
2 to serve next customer
3 to quit1
serving ticket...124
['123', '124']
1 to add to queue
2 to serve next customer
3 to quit2
['124']
1 to add to queue
2 to serve next customer
3 to quit2
[]
1 to add to queue
2 to serve next customer
3 to quit2
No tickets in queue
[]
1 to add to queue
2 to serve next customer
3 to quit3
[]
>>>
```

## Task 2

Modify this program, so a few sequentially numbered tickets are loaded into the queue automatically, rather having to enter them manually.

## Task 3

Adapt this program to accept a list of directions to a place, like on a SatNav and when the user presses `<Enter>` the directions will be stricken off the list, until all have been popped. The program will then display a message "You arrived at your destination".

---
title: Implementing stacks
files:
  - action: close
    path: "#tabs"
layout: ""
step: 10-stacks

---
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
