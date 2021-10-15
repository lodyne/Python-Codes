#A list is a collection which is ordered and changeable. i.e mutable
x = ["a",'e','t',6,8,9] 
print(x)  
print(x[1:4])
y=[9,0,4,2]                 #In Python lists are written with square brackets.
print(y)
z=["oya","hey","au sio"]
print(z)

print(len(x))               #determine how many items a list have
print(x[1])
print(x[-1])
print(x[5])
print(x[2:4])
print(x.index('t'))         #return the index value of the object
x.append(10)                #add an item to the end of the list
print(x)
x.insert(2,'A')             #add an item at the specified index
print(x)
if 6 in x:
    print('yes')
else:
    print("no")
for list in x:
    print(list)
print(x.remove("a"))       #removes the specified item
print(x.pop())             #removes the the last item if index is not specified
print(x.pop(3))            #removes the specified index
del x[3]                   #removes the specified index
print(x)
print(x.extend(y))         #add a sequence to the existing list
print(x.copy())            #Returns a copy of the list
print(x.reverse())         #Reverses the order of the list
print(y.sort())            #Sorts the list
print(z.count('oya'))      #Returns the number of elements with the specified value
print(x.clear())           #Removes all the elements from the list

# !Python List Methods

# They are accessed as list.method() . 
'''
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the deÒned index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the Òrst matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list
'''
