# DUNDER METHODS
class Profile: 
    def __init__(self,firstname,secondname,age):
        self.firstname = firstname
        self.secondname = secondname
        self.age =age
        self.email = firstname + '.'+secondname+ '@gmail.com'
        
    # def fullname(self):
    #     return (
    #         f" My name is {self.firstname} {self.secondname} and I'm {self.age}"
    #     )

    def display_email(self):
        print(self.email)
    
    #* An ambiguous representation of the object, 
    #* used for debugging & meant to be seen by developers
    def __repr__(self):
        return (f"{self.firstname}-{self.secondname}-{self.age}")

    #* A readable representation of the object
    #* meant to be as display for end users 
    def __str__(self):
        return (f" My name is {self.firstname} {self.secondname} and I'm {self.age}")

    #* Dunder Arithmetic Methods 
    def __add__(self,other):
        return self.age + other.age

    def __sub__(self,other):
        return self.age - other.age

    def __mul__(self,other):
        return self.age * other.age

    def __truediv__(self,other):
        return self.age/other.age

    def __len__(self):
        return len(self.email)

obj1 = Profile('Lody','Mtui',28)
obj2 = Profile('Lui','  Mtui',24)

print(obj1 + obj2)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1/obj2)

#* This print object
# print(obj1)

#* This print the messages of called functions
# print(obj1.fullname())
# obj1.display_email()

#* This print the messages from special functions
print(repr(obj1))
print(str(obj1))
print(obj1.__len__())
print(len(obj2))

# print(obj1.__str__())
# print(obj1.__repr__())





