class Employee:
    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.email = last_name + '.' +first_name+ '@gmail.com'

    
    # def fullname(self):
    #     return f"{self.first_name} {self.last_name}"

    # def getEmail(self):
    #     return f"{self.first_name}.{self.last_name} @gmail.com"

    # * Using property decorator

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def getEmail(self):
        return f"{self.first_name}.{self.last_name} @gmail.com"

    @fullname.setter
    def fullname(self,name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name =last_name
    
    @fullname.getter
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
        
        

    @property
    def getEmail(self):
        return f"{self.first_name}.{self.last_name} @gmail.com"

emp1 = Employee('Lody','Mtui')


# emp1.first_name = 'Lui'

# set up a full name
emp1.fullname = 'Paul Pogba'

# get a full name
print(emp1.fullname)

# print(emp1.first_name)
# print(emp1.last_name)

# print(emp1.fullname())
# print(emp1.getEmail())

# * With property decorator, you can call/access methods as attribute
# print(emp1.getEmail)
# print(emp1.fullname)