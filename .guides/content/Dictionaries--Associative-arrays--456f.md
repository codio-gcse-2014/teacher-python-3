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
