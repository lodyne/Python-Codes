class Mimi:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    #def display_info(self):
        #return f"My name is {self.name} and i am {self.age}"

class Main:
    obj=Mimi('Lody',25)
    #print(obj.display_info())           #calling by instantiated object

    #print(Mimi.display_info(obj))       #calling by class Name and passing object as parameter
