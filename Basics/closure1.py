def calculate(function):
    
    def inner(*args):
        print(function(*args))
    return inner

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

add_object = calculate(add)
sub_object = calculate(sub)

print(add_object)  
add_object(2,7)
sub_object(12,7)