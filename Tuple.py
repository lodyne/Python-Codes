# A tuple is a collection which is ordered and unchangeable(immutable).
x=("banana","cherry","nanasi",7,9,0)         
print(x)                                    #In Python tuples are written with round brackets.
y=tuple(("soft","tele","cs","32","java"))   #It is also possible to use the tuple() constructor to make a tuple.
print(y)
z=x,(6,'s',4,'hey')                         #creating tuple that contains another tuple
print(z)
print(x[1])
print(x[0])
print(x[-2])
#x[2]="embe"                                #Once a tuple is created, you cannot change its values.Tuples are unchangeable.
for mytuple in x:                           #Iterate through the items and print the values
    print(mytuple)
if "nanasi" in x:                           #To determine if a specified item is present in a tuple
    print("yes")
print(len(x))                               #To determine how many items a tuple has
print(x.index(0))                           #Searches the tuple for a specified value and returns the position of where it was found
print(x.count(7))                           #Returns the number of times a specified value occurs in a tuple
"""del x #The del keyword can delete the tuple completely:
print(x) #this will raise an error because the tuple no longer exists"""