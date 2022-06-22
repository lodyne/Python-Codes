def increment(num):
    return num + 1

def decrement(num):
    return num -1

def operation(function,num):
    result = function(num)
    return result

print(operation(increment,4))
print(operation(decrement,4))
