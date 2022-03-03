# Decorator is a function that takes another function as
# an argument, adds functionality and returns another function
# without altering the source code of the original function we pass in
def outer_function(sms):
    # msg = sms
    def inner_function():
        # print(msg)
        print(sms)
    return inner_function()

func1=outer_function('bye')
func2=outer_function('hi')


