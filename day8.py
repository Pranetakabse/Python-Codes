### If statement
## is a block of code that allows you to control the path the computer will take when it executes your code.
'''
logical operators
- equals : a == b
- not equals: a !=b
- Less than: a< b
- Less than or equal to: a <= b
- Greater than: a>b
- Greater than or equal to: a>=b

'''
# Check if b is greater than a

a = 33
b = 200

if b > a:
    print("b is greater than a")


#indentation - whitespace at the begining of the line

## if statement, without indentation (will raise an error)
# if a is greated than b
'''
a = 45
b = 20

if a > b:
print("a is greater than b")
'''

mood = 'tired'
if mood == 'tired':
    
    hit_snooze_button = True
    print("Anna is tired. She hits the snooze button.")


#elif - if the previous conditions were not true, then try this condition.

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

    
mood = 'well-rested'
if mood == 'tired':
    
    hit_snooze_button = True
    print("Anna is tired. She hits the snooze button.")

elif mood == 'well-rested':
    get_out_of_bed = True
    print("Anna is well-rested. She's already out of bed.")


### else - else keywaord catches anything which isn't caught by the preceding conditions.


a = 200
b = 33
if b > a:
    print("b is greater than a")

elif a == b:
    print("a and b are equal")

else:
    print("a is greater than b")


## you can also have an else without elif.

a = 200
b = 33
if b > a:
    print("b is greater than a")

else:
    print("a is greater than b")



##And - and keyword is a logical operator, ans is used to combine conditional statement
'''
Test if a is greater than b,

AND if c is greater than a
'''

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

## OR - or keyword is a logical operator, and is used to combine conditional statements.
'''
Test if a is greater than b,

OR if a is greater than c
'''

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the condition is True.")


## NOT - not keyword is a logical operator, and is used to reverse the result of the conditional statement

    
'''

Test if a is not greater than b
'''

a = 33
b = 200
if not a > b:
    print("a is not greater than b")














































































































    
