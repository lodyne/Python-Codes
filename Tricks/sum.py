def sumOfNumbers(num):
    sum = 0
    for i in range(2,num+1):
        sum = sum + i
    return sum
summmation = int(input("enter number: "))
print(sumOfNumbers(summmation))
