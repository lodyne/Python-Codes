def sum(a,b):
    z=a+b
    print(z)
sum(7,3)

def sms():
    print('this is it')
sms()

def mult(x,y):
    return x*y
print(mult(4,3))

def abs_val(x):
    if x>=0:
        return +x
    else:
        return -x
print(abs_val(-2))
print(abs_val(4))

def greet(name,sms="Hello"):
    """
    This function greets to the person with the provided message.
    If message is not provided,it defaults to "Good morning!"
    """
    print(name+" "+sms)
greet("Lui")
greet("Lody","Good Morning") 
greet("Lody",sms="Morning") # keyword arguments must follow positional arguments
# greet(name='LODY',"Safi safi?") Error:positional argument follows keyword argument 
greet(name="Jay",sms="Uko poa?")
greet(sms="Niaje",name="chalii") 

def list_name(*names):
    for name in names:
        print("Hello",name)
list_name('Chair','Reico','Side',"Sam")