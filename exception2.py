try:
    num1=float(input('Enter number 1:'))
    num2=float(input('Enter number 2:'))

    def divide():
        result = num1/num3
        return result
    print(divide())

except NameError as b:
    print (b)

except Exception as a:
    print (f"Can't divide this due to {a}")

else:
    print("Executed")

finally:
    print("Finally Done")