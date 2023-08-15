####Function - is a block of code which runs when it is called.
#pass - data, know as parameters, into a function

## create a function

def my_function():
    print("Hello from a function")

my_function()


#### Arguments

def my_function(fname):
    print(fname + " Ford")

my_function("John")
my_function("Anna")


##### Number of Arguments

## This function expects 2 arguments, and gets 2 arguments.

def my_function(fname, lname):
    print(fname+ " " + lname)

my_function("Megan", "Ford")



####Arbitrary Arguments, *args

#If the number of arguments is unknown, add a * before the parameter name:


def my_function(*kids):
    print("The youngest child is " +kids[3])

my_function("John", "Anna", "Megan", "Linus")



####Keyword Arguments - key = value syntax

def my_function(child3, child2, child1):
    print("The youngest child is " +child3)


my_function(child2="Anna", child1="Megan", child3='Linus')


### Arbitrary Keyword Arguments, **kwargs


def my_function(**kid):
    print("His first name is "+kid["fname"])

my_function(fname="Bob", lname="Ford")



#### Default Parameter value

def my_function(country = "India"):
    print("I am from "+ country)

my_function("Sweden")
my_function()
my_function("Brazil")

#### Passing a List as an Argument

def my_function(fruits):
    for x in fruits:
        print(x)

fruits = ["apple", "banana", "cherry"]


my_function(fruits)



























































