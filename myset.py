#A set is a collection which is unordered and unindexed. 
x={"apple","samsung",5,"tecno","nokia","a","hey"} 
print(x)                                          #Note: Sets are unordered, so the items will appear in a random order.
y={1,2,3,4,5,'a','e','i','o','u'}                 #In Python sets are written with curly brackets.
print(y)
for set in x:                                     #Loop through the set, and print the values
    print(set)
if "4" in x: 
    print("yes")
elif "tecno":
    print("maybe")
else:
    pass
print("banana" in x)
print("apple" in x)
x.add("itel")                                   #To add one item
print(x)
x.update([30,"htc","mimi"])                     #To add more than one item
print(x)
print(len(x))                                   #To determine how many items a set has
                                                #To remove an item in a set, use the remove(), or the discard() method.
x.remove("tecno")                               #If the item to remove does not exist, remove() will raise an error.
print(x)
x.discard("htc")                                #If the item to remove does not exist, discard() will NOT raise an error.
print(x)
A={1,2,3,4}
B={3,4,5,6}
print(A|B)
print(A&B)
print(A-B)
print(B-A)

A.union(B)
A.intersection(B)
A.difference(B)
A.symmetric_difference(B)

