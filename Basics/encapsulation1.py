class Student:
    
    def __init__(self, name, age, address, accountno):
        self.name = name
        self.age = age
        self.address = address
        self.accountno = accountno
    

    def set_age(self, age):
        self.age = age
    
    def get_age(self):
        return self.age

    def set_name(self, name):
        self.age = name
    
    def get_name(self):
        return self.name

    def set_address(self, address):
        self._address = address
    
    def get_address(self):
        return self.address

    def set_account(self, accountno):
        self._address = accountno
    
    def get_account(self):
        return self.accountno


class Main:
    std =  Student("lodger",17,"dsm",12345,)

    std.set_name('lodri')
    std.set_age(72)
    std.set_address('dom')
    std.set_account(98772)

    print(f"My age is {std.get_age()}")
    print(f"My address is {std.get_address()}")
    print(f"My name is {std.get_name()} ")
    print(f"My account number is {std.get_account()}")
    

    
    
    

    