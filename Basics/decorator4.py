def decorator(function):
    def inner(num):
        result = num * num
        print(result)  
        function()
    return inner


def square(msg):
    msg = "square"
    print(msg)

obj = decorator(square)
obj(2)
