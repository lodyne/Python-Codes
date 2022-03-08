def beautify(function):
    def inner():
        new = function("mimi")
        print(new)
        
    return inner
    
def normal():
    print("i'm normal")
object = beautify(normal)
print(object)
object

# def beautify(function):
#     def inner():
#         print("i'm decorated")
#         function()
#     return inner
    
# def normal():
#     print("i'm normal")
# normal = beautify(normal)
# normal()