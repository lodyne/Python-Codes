import datetime

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    
    @classmethod
    def date_of_employed(cls,name,year):
        return cls(name,year)
        print (f'Name is {name} and year is {year}')
        
    #Used to create utility functions
    @staticmethod
    def is_workday(day):
        if day == 5 :
            return False
        else:
            return True

emp1=Employee("Pogba",27)
emp2=Employee.date_of_employed("Pogba",1997)
print(emp1.name)
print(emp2)

print(Employee.is_workday(0))