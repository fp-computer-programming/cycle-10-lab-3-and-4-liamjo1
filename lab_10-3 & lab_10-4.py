"""

Create a Python file named lab_10-3.py
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a program that contains a function called double_stuff. The function should take a list as its only parameter.
When a list is passed as an argument to the function, the function should double each value in the list, regardless of its type
Write test cases to confirm that your function works when passed a list that:
Contains only integers
Contains integer and float values
Contains a combination of integer, string, and float values

_____________________________________________________________________________________________________________

Create a Python file named lab_10-4.py

Write a program that contains a function called indexed_names. 
The function should take a list of names as its only parameter.
When a list is passed as an argument to the function,
the function should return a new list where each value is replaced by the index, 
followed by a color, space, and the original value
i.e. passing through ["John", "Jane", "Bob"] 
would return ["0: John", "1: Jane", "2: Bob"]
Write 2 test cases to confirm that your function works when passed a list that:



"""
# Lab 10-3

# Author: Liam O'Hara

list = [] # "list" makes a blank list

listd = [] # "listd" creates another blank list

ph = int(0) # "ph = int(o)" sets the placeholder equivalent to 0
def double_stuff(list):

    ph = 0
    while len(listd) != len(list): # the list doesn't have every value

        doubv = list[ph] # Doubles the list 

        listd.append(2*doubv) # Doubled list added to the new value 

        ph = ph + 1 # Moves over one value

    print (listd)

double_stuff([1, 2, 3, 4, 5, 6, "s"])

# Lab 10-4

list = [] # "list" equals blank space

indname = [] # "indname" makes a blank list

def indexed_names(list):

    ph = 0 # creates the placeholder and equals it to 0

    while len(indname) != len(list): # this makes sure the lists are equal to the same length

        name = list[ph] # Lists a word 

        rep = [ph, ": ", name] # tells you what to add

        indname.append(rep) # and then adds it

        ph = ph + 1 # moves it over one space 

    print(indname)

names = ["Caleb", "Matthew", "Liam"]

indexed_names(names)