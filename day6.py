###List
# Lists are mutable

my_favorite_dessert = []
print(my_favorite_dessert)

my_favorite_dessert = ['Brownies', 'Muffins', 'chocolate']

print(my_favorite_dessert)

my_favorite_dessert += ['cake']
print(my_favorite_dessert)

my_favorite_dessert += ['Lava cake']
print(my_favorite_dessert)

#append()

my_favorite_dessert.append('Apple Pie')
print(my_favorite_dessert)


#remove()

my_favorite_dessert.remove('Muffins')
print(my_favorite_dessert)

#del()

del my_favorite_dessert[1]
print(my_favorite_dessert)

del my_favorite_dessert[1:]
print(my_favorite_dessert)


#Changes using Indices and slice ranges

my_favorite_dessert[1:1] = ['pumpkin pie']
print(my_favorite_dessert)

my_favorite_dessert[1:1] = ['pie']
print(my_favorite_dessert)



####TUPLES

#TUPLES- are similar to lists that hold a collection of items or objects.

# tuples use paranthese

#rgb_colors = ('red, 'green', 'blue')
#print(rgb_colors)

# Tuples are immutable - we are unable to change.
# methods like append(), remove() function and del() will not work with tuples.


my_favorite_dessert = ['Brownies', 'Muffins', 'chocolate', 'Brownies']
              
print(my_favorite_dessert)


rgb_colors = ('red', 'green', 'blue', 'red')
print(rgb_colors)
print(len(rgb_colors)) # to check the length use len() function


thistuple = ("apple")
print(type(thistuple))


tuple1 = ("apple", "banana", "cherry")

tuple2 = (1, 2, 3, 5, 56)

tuples3 = (True, False, True)

tuples4 = ("cherry", 45, True)


####sets

#sets is a collection which is unordered, unchangeable, and unindexed.

thisisset = {"apple", "banana", "cherry","apple"}
print(thisisset)


thisisset = {"apple", "banana", "cherry","apple","banana"}
print(thisisset)


thisisset = {"apple", "banana", "cherry", True, 2}

print(thisisset)

print(len(thisisset))

print(type(thisisset))


thisisset = {"apple", "banana", "cherry"}

print(type(thisisset))



### create a list and check its type and length. 
































