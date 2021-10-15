class Employee:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.email=fname+ ''+lname+ '@gmail.com'
        #print(self.email.lower())
        
    
    def full_name(self):
        return '{} {}'.format(self.fname,self.lname)
        #print('{} {}'.format(self.fname,self.lname))
    
    def display(self):
        return 'Name:{} Age:{} Email:{}'.format(self.full_name(),self.age,self.email.lower())
        #print ('Name:{} Age:{} Email:{}'.format(self.full_name(),self.age,self.email.lower()))

    def __repr__(self):
        return f'Name: {self.full_name()}; Age: {self.age}; Email: {self.email}'
        
    def __str__(self):
            return f'Name: {self.full_name()}; Age: {self.age}; Email: {self.email}'

    def __add__ (self,other):
        return self.age + other.age

    def __len__ (self):
        return len(self.full_name())    
        
emp1=Employee('Lody','Mtui',26)
emp2=Employee('Lui','Mtui',22)
print(emp1)
print(repr(emp1))
# print(emp1.__repr__())

print(str(emp1))
# print(emp1.__str__())

print(len(emp1))
print(len(emp2))

print(emp1 + emp2)
# print(len('test'))
# print('test'.__len__())