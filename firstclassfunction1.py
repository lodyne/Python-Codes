"""
Python's Function are First Class Functions means that:
~ you can assign them as variable,
~ you can store them in data structures,
~ you can pass them to other functions as arguments, 
~ you can return them from other functions as values.

"""
#* PROPERTIES OF FIRST CLASS FUNCTION

# 1: A function is an instance of the Object type.
def power(num1,num2):
    return num1 ** num2

# assigning INSTANCE to function
result1= power(2,3)
print(power)
print(result1)


# 2: You can store the function in a variable
def square(num):
    return num*num

# store the function in a variable
result2 = square
print(result2)
print(result2(3))

# 3: You can pass the function as a parameter to another function.
def morning():
    return "good morning"

def noon():
    return "good afternoon"

# high order function    
def greetings(function):
    greet = function()
    print(greet)

greetings(morning)
greetings(noon)

def my_map(func,list):
    result=[]
    for i in list:
        result.append(func(i))
    return result

sqr = my_map(square,[1,2,3,4,5])

print(sqr)

# 4: You can return them from other functions as values.

def login_message(msg):
    def log():
        print(msg)
    return log 

log_hi = login_message('hi')
log_hi()

def outer_power(num1):
    def inner_power(num2):
        return num1 ** num2
    return inner_power

power=outer_power(4)
print(power(3))


