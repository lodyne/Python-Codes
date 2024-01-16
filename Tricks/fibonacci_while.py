number = int(input("How many terms? "))

num1, num2 = 0, 1
count = 0
if number <= 0:
    print("Enter positive number")

elif number == 1:
    print(num1)

else:
    print("Fibonacci Series")
    while count <= number:
        
        print(count,end=" ")
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1