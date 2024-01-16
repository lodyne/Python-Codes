def power(num1,num2):
    return num1 ** num2

#? create an instance of class
# pow = power(4,7)
# print(pow)

# ? assign function as variable
pow = power
print(pow(2,3))

print('************************')


def number1(num1):
    return num1
def printNumber(function):
    func = function(5)
    print(func)
# ? pass function as argument to another function
printNumber(number1)

def passedAsArgument():
    return 'Return passed function'

def functionToPassAnother(function):
    func = function()
    print(func)
# ? pass function as argument to another function
functionToPassAnother(passedAsArgument)