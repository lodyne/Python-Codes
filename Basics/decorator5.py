# Decorator is a function that takes another function as
# an argument, adds functionality and returns another function
# without altering the source code of the original function we pass in 
def outer_function(func):

    def inner_function():
        message = "hey"
        print(message)
        func()
    return inner_function

# def decorated_function():
#     print("hello")

# func1=outer_function(decorated_function)
# func1

@outer_function
def decorated_function():
    print("hello")
decorated_function()


