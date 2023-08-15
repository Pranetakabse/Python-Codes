### Dictionaries
# dictionaries are used to store data values in key:value pairs.

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
    }

print(thisdict)

### Print the "brand" value of the dictionary.

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
    }

print(thisdict["brand"])
print(len(thisdict))

##duplicates Not Allowed

# Duplicate values will overwrite the existing values

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964,
    "year": 2020
    }
print(thisdict)

print(len(thisdict))

#### Values in dictionary items can be of any data type


thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964,
    "electric": False,
    "colors": ["red", "white", "blue"]
    }
print(thisdict)

print(type(thisdict))

### Accessing items


thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
    }

x = thisdict["model"]
print(x)


###There is also a menthod called get() that will give the result


thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
    }

x = thisdict.get("brand")
print(x)


### Add a new item

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
    }

x = thisdict.keys()

print(x) # before the change

thisdict["color"] = "white"

print (x) # after the change


#### value() method will return a list of all the values in the dictionary

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
    }

x = thisdict.values()

print(x)


####

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
    }

x = thisdict.values()
print(x) # before the change

thisdict["year"] = 2020
print(x) # after the change


#### Add new item

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
    }

x = thisdict.values()
print(x)

thisdict["color"] = "red"

print(x)
print(thisdict)


#### get items
# item() method to return each item in a dictionary, as tuple in a list

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
    }

x = thisdict.items()
print(x)


##### Create a new dictioanry which has 5 keys and values.
#print it.
# print only keys
#print only values
# add new item (key and value) and print it. 







































































  
