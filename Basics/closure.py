# A Closure is a function object that remembers values in enclosing scopes 
# even if they are not present in memory.
# OR
# A Closure is an inner function that remembers and has access to variables
# in a local scope in which it was created even after the outer function has
# finish executing


def outer():
    sms = "hey nambie" 

    def inner():
        print(sms)
    return inner
obj = outer()
print(obj)
print(obj.__name__)
obj()
obj()
obj()

print("**************")

def outer():
    def inner(sms):
        print(sms)
    return inner
obj = outer()
print(obj)
print(obj.__name__)
obj("hey")


print("**************")

def outer(msg):
    message = msg
    def inner():
        print(message)
    return inner

# * A closure closes over the free variable from their environment  
obj1 = outer("Hi")
obj2 = outer("hello")

obj1()
obj2()

print("**************")

def outer(msg):
    # print(msg) 
    def inner(sms):
        print(f" {msg} {sms}")
    return inner

obj1 = outer("Hi")
obj2 = outer("hello")

obj1("Good Morning")
obj2("Good AfterNoon")

''' 
The criteria that must be met to create closure in Python are summarized below:

~ We must have a nested function (function inside a function).
~ The nested function must refer to a value defined in the enclosing function.
~ The enclosing function must return the nested function.

'''


