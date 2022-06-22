def beautify(function):
    def inner():
        new = "mimi"
        return function(new)
    return inner
    
def normal(old):
    old = "wewe"
    print(old)
object = beautify(normal)
object()

# def beautify(function):
#     def inner():
#         print("i'm decorated")
#         function()
#     return inner
    
# def normal():
#     print("i'm normal")
# normal = beautify(normal)
# normal()