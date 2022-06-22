#using normal way
def beautify(function): # high-order function (a function that passes another function as argument)
    def inner():
        print("i'm decorated")
        function()
    return inner
    
def normal():
    print("i'm normal")

# assign beautify function in variable new
# then, pass normal function in it
new = beautify(normal)
new()



# # using decorators
def beautify(function):
    def inner():
        print("i'm decorated")
        function()
    return inner

@beautify   
def normal():
    print("i'm normal")
normal()

'''
    ~ beautify is the decorator function i.e 
    it adds some functionality to the original function - 
    This is similar to packing a gift. 
    The decorator acts as a wrapper. 
    The nature of the object that got decorated,
    (actual gift inside) does not alter.
    ~ normal is the decorated function

    def normal():
        print("i'm normal")
    norm = beautify(normal)
    norm()

    is equivalent to

    @beautify
    def normal():
        print("i'm normal")
    normal()
    

'''

