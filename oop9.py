class Student:
    #name="Lody"
    #age="25"

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"I am {self.name} and i am {self.age} years old")

    def study(self):
        print("I am taking Bsc.SE")

class Address(Student):
    street=""
    city=""

    #def __init__(self,street,city):
        #super().__init__(self.name,self.age)
        #self.street=street
        #self.city=city
    
    def __init__(self,name,age,street,city):
        super().__init__(name,age)
        self.street=street
        self.city=city        
    
    def display(self):
        print("I am from {},{}".format(self.street,self.city))

class Main:
    #object=Address("East Zoo","Dodoma")
    object=Address("Lody",25,"East Zoo","Dodoma")
    object.display()
    object.study()



