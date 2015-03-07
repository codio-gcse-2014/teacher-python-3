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

This program will save a dictionary to a txt file. If we change the file extension to ".csv" from ".txt", we can open this file.

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

[Click Here](open_file "08-files/csv.txt") to open the created file.

