class Addition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def __add__(self, this):
        num1 = self.num1 + this.num1
        num2 = self.num2 + this.num2
        add = Addition(num1,num2)

        return add

obj1 = Addition(20,10)
obj2 = Addition(45,98)

obj3 = obj1 + obj2
print(obj3.num1)