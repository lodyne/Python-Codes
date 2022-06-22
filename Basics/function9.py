def greet(name,msg):
     print(name+ " " +msg)
#greet("Bruce", "Niaje")
greet(name="Bruce",msg="Niaje") # 2 keyword arguments

greet(msg="Niaje",name="Bruce") # 2 keyword arguments (out of order)

greet("Bruce",msg="Niaje") # 1 positional, 1 keyword argument

"""positional argument follow keyword argument"""
#greet(name="Bruce",msg) 