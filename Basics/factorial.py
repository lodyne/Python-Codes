from math import factorial


n = int(input("enter number: "))

factorial = 1

for i in range(2, n + 1):
    factorial*= i

print(factorial)