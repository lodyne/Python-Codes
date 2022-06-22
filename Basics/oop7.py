"""Single inheritance in Python"""
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # def display(self):
        # print ('My name is {}, and my age is {}'.format(self.name,self.age))

    def display(self):
        return f'The name is {self.name}, and its age {self.age}'
        

class Dog(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        #Animal.__init__(self,name,age)
        self.color=color

    def update(self):
        print("My color is {}".format(self.color))


object_1=Dog("Scooby",5,"brown")
object_2=Dog("Poppy",7,"black")

object_1.display()
object_1.update()

object_2.display()
object_2.update()

#print(issubclass(Dog,Animal))
#print(isinstance(object_1,Dog))
#print(help(Dog))

        