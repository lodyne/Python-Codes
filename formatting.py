name= 'Lui'
age= 21

print("My name is "+name) #doube quote
print('My name is '+name) #single quote

#String method - concantenation
print("My name is "+ name +" and I am "+ str(age) + " years old.")

#String method - using commas
print("My name is" ,name, "and I am" ,str(age), "years old.")

#format method
print("My name is {name} and I am {age} years old.".format(name=name, age=age))
print("My name is {} and I am {} years old.".format(name, age))

print("{} {}".format('Hello','World'))

#f-string
print(f"My name is {name} and I am {age} years old.")

