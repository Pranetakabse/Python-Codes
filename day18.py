### Class
'''
class MyClass:
    x = 5

a1 =  MyClass()

print(a1.x)
'''
print("-----------------------------------------------")
######### The __str__() Function

### WITHOUT the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1  = Person("John", 16)

print(p1)
print("-----------------------------------------------")

### WITH __str__() function:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 16)

print(p1)



### Object Methods


#Insert a function that prints a greeting, and execute it on the p1 object:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def myfunc(self):
        print("hello my name is " +self.name)

p1 = Person("John", 16)
p1.myfunc()


#### Self Parameter - is used to access variables that belong to the class.
# self Parameter - It does not have to be named "self", you can call it whatever you want

## Modify the Object Properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello my name is " +self.name)

p1 = Person("John", 16)

p1.age = 36
p1.name = "Megan"

print(p1.age)
print(p1.name)


### Delete Object Properties:

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello my name is " +self.name)

p1 = Person("John", 16)

del p1.age

print(p1.age)

'''
## Delete Object


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello my name is " +self.name)

p1 = Person("John", 16)

del p1

print(p1)








































































