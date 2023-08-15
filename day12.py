###LOOPS : There are 2 kinds of main loops
#1. FOR LOOP
#2.WHILE LOOP

### FOR LOOP

#Iteration - means going through a group of things one by one.

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number + 2,"-----------------")
'''
#Syntax:

for <iterator> in <group of items>:

'''
'''
The range() function - The range() function returns a sequence of numbers,
starting from 0 by default, and increments by 1(by default), and ends at a
specified number. 

'''
for i in range(3):
    print(i)
    

for i in range(10, 21):
    print(i)

for i in range(0, 101, 10):
    print(i)

#### for loop using tuple.

fruits = ("apple", "banana", "cherry")
for x in fruits:
    print(x)

## Loop through the letters in the word "banana"

for x in "banana":
    print(x)

### The break statement

# Exit the loop when x is "banana"

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
print("-------------------------------------")

# Exit the loop when x is "banana", but this time the break comes before the print

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x =="banana":
        break
    print(x)

print("-------------------------------------")
###The continue Statement

fruits = ["apple", "banana", "cherry", "rice"]
for x in fruits:
    if x == "banana":
        continue
    print(x)














    



























