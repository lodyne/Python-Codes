# A tuple is a collection which is ordered and unchangeable(immutable).
# Trick to make tuple mutable

mytuple = (1,"yanga",7.89, "simba")
print(mytuple)

# throw an error, since tuple is immutable
# mytuple[1] = 'azam' 

# change tuple to list
listedtuple = list(mytuple)
print(listedtuple)

# you can change to other values since list is muttable
listedtuple[1] = 'azam'
print(listedtuple)

#return it back to tuple
newtuple = tuple(listedtuple)
print(newtuple)
