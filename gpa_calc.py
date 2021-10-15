#SYSTEM TO CALCULATE GPA
class GPA:
    grade=None
    credit=None
    course=None

    def getgrades(self):
        self.grade=int(input("Enter grades  "))
        

    def getgradedata(self):
        num_of_grades={'A':5,'B':4,'C':3,'D':2,'E':1,'F':0}
        x=num_of_grades[self.grade]
        return x

    # def getcredits(self):
    #     if units is 7 and 10:
    #         course=int(input("Enter course units"))
    #     else:
    #         print("Invalid")        





object=GPA()
x=object.getgradedata()   
print(x)  