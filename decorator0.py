# Syntax of Python Decorator
'''Python decorators allow you to change the behavior 
of a function without modifying the function itself.'''

def decorator_function(function):
    def inner_function():
        # Do smthn before the function
        function()
        # Do smthn after the function
    return inner_function

'''To use a decorator place the name of the decorator directly 
with an @ symbol above the function we want to use it on '''

@decorator_function
def decorated_function():
    print('anything')
decorated_function()