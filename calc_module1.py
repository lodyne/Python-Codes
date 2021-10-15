class Calculator:

    def add(self):
        sum=a+b
        return sum
    
    def substract(self):
        sub=a-b
        return sub
    
    def multiply(self):
        product=a*b
        return product
    
    def division(self):
        div=a/b
        if b < 0:
            return 'Error'
        else:
            return div

obj=Calculator()
a=int(input("enter first number "))
b=int(input("enter second number "))

print(obj.add())
print(obj.division())
