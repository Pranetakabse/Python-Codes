'''
#### Python Object Oriented Programming

#Objects - An object is any entity that has attributes and behaviors.

- attribues - name, age, color, etc

- behavior - dancing, singing, etc

# Class - is considered as a blueprint of objects, prototype,

## syntax:

class ClassName:
    # class definition





class Bike:
    name = " "
    gear = 0


# The variables inside a class are called attributes.

#Objects are the instance of a class
Syntax:

objectName = ClassName()



bike1 = Bike()


#modify the name attribute

bike1.name = "Mountain Bike"

bike1.gear = 11

'''
#### Pyhton Class and Objects

class Bike:
    name = " "
    gear = 0


bike1 = Bike()

bike1.name = "Mountain Bike"
bike1.gear = 11

print(f"Name: {bike1.name}, Gears: {bike1.gear}")

'''
#### Key points to remember

- OOPM makes program easy to understand as well as efficient.
-  code can be reused

- Data is safe


####
'''
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)


### The __init__() function

# Create a class named Person, use the __init__() function to assign values for
#name and age:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 16)


print(p1.name)
print(p1.age)



### Create a class named Person, use the __init__() function to assign values for
#name,age, school and last name



































