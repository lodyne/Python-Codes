from math import factorial


def factorize(num):
    factorial = 1
    if num > 0:
        for i in range(1, num+1):
            factorial = factorial * i
        return factorial
    else:
        print("factorial doesn't exist")
        
number = int(input("enter number: "))
print(f"The factorial of {number} is: ")
print(factorize(number))
