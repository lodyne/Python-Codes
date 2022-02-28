try:
    num1=float(input('Enter number 1:'))
    num2=float(input('Enter number 2:'))

    def divide():
        result = num1/num2
        return result
    print(divide())

except ZeroDivisionError:
    print ("Can't divide by zero")
    print(Exception)

else:
    print("Executed")