def decorator_function(original_function ):
    def wrapper_function():
        return original_function
    return wrapper_function()

def display():
    print("run function")

decoratored_function = decorator_function(display)
decoratored_function ()
