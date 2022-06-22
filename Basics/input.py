print("Enter your full name")
x=input()
print("My name is  "+x)


radius=int(input("Radius is: "))
Area=3.14*radius**2
print("Area of a circle is=",Area)

#USING format() method
num1=678.970505064
num2=5.34560143206
print("number 1 is {0:.2f} and number 2 is {1:.3f}".format(num1,num2))

#USING f-string
print(f"number 1 is {num1:.2f} and number 2 is {num2:.3f}")