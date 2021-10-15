name="Lui"                                 #global variable

def introduction():
    age=17                                 #local variable
    print(age)
    print(name)
introduction()

def local_global():
    name="Lody"
    print("Inside the function: "+name)
local_global()
print("Outside the function: "+name)

def update():
    global name                            #use global keyword to read and write a global variable inside a function
    name=name*2                            #global variable can only be accessed but cannot be modified
    print(name)
update()

def another_one():
    job="director"
    print("My job is "+job)
another_one()
#print("My job is "job)                   #local variable works only in local scope

def outer_fuction():                      #nested function using global keyword
    title="student"

    def inner_fuction():
        global title
        title="lecturer"

    print(title)
    inner_fuction()
    print(title)


outer_fuction()
print(title)


