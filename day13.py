###The while loop - with the while loop we can execute a set of statements as long
#as the condition is true.

# Print i as long as i is less than 6:

i = 1
while i < 6:
    print(i)
    i += 1

print("---------------------------")

####The Break Statement - we can stop the loop even if the while condition is true


# Exit the loop when i is 3:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
    
print("--------------------------")
#####The continue Statement - we can stop the current iteration, and continue with the next

# Continue to the next iteration if i is 3:

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)

print("--------------------------")
    

##### The else statement - we can run a block of code once when the condition no longer is true

## Print a message once the condition is false.

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print(" i is no longer less than 6")


print("--------------------------")
    
####FOR LOOP

people = ['Mario', 'Peach', 'Daisy', 'Toad']
desserts = ['Star Pudding', 'Peach Pie', 'Honey Cake', 'Jelly Beans']

for i in range(len(people)):
    name = people[i]
    dessert = desserts[i]
    print(f"Hi! My name is {name}. My favorite dessert is {dessert}.")



#### Check if number is greater than 0 (using if condition)

number = 10 

if number > 0:
    print("Number is greater than 0")

print("--------------------------")
### Check if number is greater than 0 (using if and else condition)


number = 10 

if number > 0:
    print("Number is greater than 0")
else:
    print("Number is not greater than 0")




    

