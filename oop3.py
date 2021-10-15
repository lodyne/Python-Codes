class Greetings:
    def myfunction(self,name):
        self.name=name
        print("Hello " +name+ ".Morning") 


    def greet(self,name="Lui"):
        print("Hello " +name)

obj=Greetings()
obj.myfunction("Lody")
obj.greet()