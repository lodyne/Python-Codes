class Employee:
    raise_amount=1.04
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=self.fname.lower()+''+ self.lname.lower() + '@gmal.com' 

    def fullname(self):
        # return '{} {}'.format(self.fname,self.lname)
        return f' My name is {self.fname} {self.lname}'

    def apply_raise(self):
        return 'Payrise: {}'.format(int(self.pay * self.raise_amount))

    @classmethod
    def function_to_raise_amount(cls,amount):
        cls.raise_amount=amount

class Department(Employee):
    def __init__(self,dname,title):
        self.dname=dname
        self.title=title

    def assign_role(self):
        print(f"{self.dname}:{self.title}")
    
Employee.function_to_raise_amount(1.05)
 
emp1=Employee('Lodger','Mtui',50000)
emp2=Employee('Luis','Mtui',60000)
dep=Department("CSE","HoD")
# print(emp2.fullname())
# print(Employee.fullname(emp2))
#print(emp1)
#print(emp2)

#emp1.name="Lodger"
#emp1.email="lodgmtui@gmail.com"

#emp2.name="Luis"
#emp2.email="lui@gmail.com"
print(dep.assign_role())


print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(emp1.raise_amount)
print(emp1.apply_raise())