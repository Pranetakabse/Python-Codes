###Array -
#- arrays are used to store multiple values in one single variable

##create an array containing car names:

cars = ["Ford", "volvo", "BMW"]
print(cars)


#### get the value of the first array item

cars = ["Ford", "volvo", "BMW"]

x = cars[0]

print(x)


##modify the value of the first array item

cars = ["Ford", "volvo", "BMW"]

cars[0] = "Toyota"

print(cars)


###length of the array

cars = ["Ford", "volvo", "BMW"]
x = len(cars)
print(x)


###Looping Array Elements


cars = ["Ford", "volvo", "BMW", "Tesla"]

for x in cars:
    print(x)

    

###Adding Array Elements (append)

cars = ["Ford", "volvo", "BMW", "Tesla"]

cars.append("Honda")

print(cars)


###Removing Array Elements (pop)


#Delete the second element of the cars array:

cars = ["Ford", "volvo", "BMW", "Tesla"]

cars.pop(1)

print(cars)


#### Delete the element that has the value "BMW" (remove)

cars = ["Ford", "volvo", "BMW", "Tesla"]

cars.remove("BMW")

print(cars)


### reverse() - reverse the order of the list

cars = ["Ford", "volvo", "BMW", "Tesla"]
cars.reverse()
print(cars)


