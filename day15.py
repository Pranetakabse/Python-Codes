### Return Value


def my_function(x):
    return 5 * x

print(my_function(3))


### Lambda
#- A lambda function can take any number of arguments,
#but can only have one expression

'''
syntax:

lambda arguments : expression

'''

# Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(11))

# Multiply argument a with argument b and return the result

x = lambda  a, b : a * b
print(x(5, 6))

# Add argument a, b and c and return the results.


###### Use the function definition to make a function that always doubles the
#number you send in

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


#### Use the function definition to make a function that always triples the
#number you send in


def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#### Use the same function definition to make both function double and triple


def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
























