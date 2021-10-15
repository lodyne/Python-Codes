def func1():
    return "Hello"

print(func1())
#print(func1().upper())
#print(func1().lower())
#print(func1().capitalize())


def func2():
    print("Hello Lodger")
func2() 

def func3(greeting):
    return '{} You'.format(greeting)
print(func3('Hi') )

def func4(greeting,name):
    return '{} {}'.format(greeting,name)
print(func4('Hi','Paul'))


 
def func5(greeting,name='Lui'):
    return '{} {}'.format(greeting,name)
print(func5('Hey'))
print(func5('Hey','Lody'))
print(func5(greeting='Hey',name="Jesse"))
print(func5('Hi',name="Jesse"))
#Required positional argument have to come before keyword arguments
#i.e print(func5('positonal arg','keyword arg'))
#print(func5(greeting='Hey',"Jesse"))

