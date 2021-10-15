def beautify(function):
    def inner():
        print("i'm decorated")
        function()
    return inner
    
def normal():
    print("i'm normal")
# normal()

new = beautify(normal)
new()

# using normal way
def beautify(function):
    def inner():
        print("i'm decorated")
        function()
    return inner
    
def normal():
    print("i'm normal")
normal = beautify(normal)
normal()

# using decorators
def beautify(function):
    def inner():
        print("i'm decorated")
        function()
    return inner

@beautify   
def normal():
    print("i'm normal")
normal()
