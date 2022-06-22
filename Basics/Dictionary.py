#A dictionary is a collection which is unordered, changeable(mutable) and indexed.
x = {                                     
    'brand':'Toyota',                   #In Python dictionaries are written with curly brackets
                                        #and they have keys and values.
    'model':'VX',
    'year':2018
}
print(x)

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict)

y=dict(name="Lui",age=21,job="director") #the dict() constructor to make a dictionary
print(y) 

z=dict({1:"Lody",2:"Mtui"})
print(z)

dictionary=x["model"]                   #accessing item via a key and square brackets
print(dictionary)
print(z[1])

dictionary=x.get("year")                #accessing using get() function
print(dictionary)
z["age"]=27                             #adding item to dictionary
print(z)
x["color"]="red"                        #Adding item to dictionary
y['job']='videographer'                 #updating value inside dictionary
print(y)
print(x)
x.pop("model")                         #removing specified item from dictionary
print(x)
x.popitem()                            #removing last item from dictionary
print(x)
del x["brand"]                         #deleting specified item from dictionary
print(x)
x.clear()                              #clear the entire dictionary
print(x)

# *Python Dictionary Methods
'''
clear()- Remove all items from the dictionary.

copy()-Return a shallow copy of the dictionary.

fromkeys( seq [,v ])-Return a new dictionary with keys from seq and value equal to v
(defaults to None ).

get( key [, d ]) -Return the value of key . If key doesnot exit, return d (defaults toNone ).

items()- Return a new view of the dictionary's items (key, value).

keys()- Return a new view of the dictionary's keys.

pop( key [, d ])- Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError .

popitem()- Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.

setdefault( key [, d ])- If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None ).

update([ other ])- Update the dictionary with the key/value pairs from other , overwriting existing keys.

values()- Return a new view of the dictionary's values
'''