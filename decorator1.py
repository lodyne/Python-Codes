# 1- A function is an object

def function():
    print(" I am function")
function()
object = function # create an object
object()

# 2- A function can be nested within another function

def outer_function():
    def inner_function():
        print("I'am nested function")
    inner_function()
outer_function()

# 3- A function can be returned

def outer():
    message = 'Ratchet happy birthday'
    def inner():
        print(message)
    return inner
new = outer()
new()

# 4 - A function can passed to another function as argument

def remainder(daily):
    # daily = "Don't forget to pray"
    # print(daily)
    print("Don't forget to pray")
    daily()

def reply():
    print("I don't remember to forget")
print(remainder(reply))
