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
