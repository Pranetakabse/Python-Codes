#####Python Inheritance - Inheritance allows us to define a class that inherits
# all the methods and properties from another class.

# Parent class - is the class being inherited from, also called base class.
# Child class - is the class that inherits from another class, also called as derived class.


### Create a class named Person, with firstname and lastname properties,
#and a printname method:


## We have created Student class which has same properties
#and methods as the Person class.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()


## Pass - Use the pass keyword when you do not want to add any other properties
# or methods to the class


### Use th Student class to create an bject, and then execute the printname method:


### __init__() function - The __init__() function is called automatically every time
# the class is being used to create a new object.


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
   


x = Student("Mike", "Olsen")
x.printname()


### super() FUnction - Super() FUnction that will make the child class inherit
# all the methods and properties from its parent class.

## By using super() function, you do not have to use the name of the parent element,
#it will automatically inherit the methods and properties from its parents. 

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
   


x = Student("Mike", "Olsen")
x.printname()

print("--------------------------------------------------")
### Add properties

## Add a property called graduationyear to the Student class:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2023
   

x = Student("Mike", "Olsen")
x.printname()
print(x.graduationyear)


##Add a year parameter, and pass the correct year when creating objects:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
   

x = Student("Mike", "Olsen", 2020)
x.printname()
print(x.graduationyear)


#### Add a method:

# Add a method called "welcome" to the "Student" class:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
   

x = Student("Mike", "Olsen", 2020)
x.welcome()














