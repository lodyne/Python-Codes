number = int(input("Enter how many terms: "))
num1 = 0
num2 = 1
count = 0

if number <= 0:
    print("Enter positive number")

else:
    print("Fibonacci series")
    for i in range(0,number):
        
        print(count, end = " ")
        num1 = num2
        num2 = count
        count = num1 + num2
        