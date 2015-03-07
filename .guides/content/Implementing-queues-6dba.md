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
