# class is a blueprint for creating instances
class Student:
    # Class variables are shared among all instances in the class
    grades={
        "A":5,
        "B+":4,
        "C":3,
        "D":2,
        "E":1,
        "F":0
    }
    number_of_students=0
    location="Tanzania"
    def __init__(self,fname,lname,age):
        # instance variables contain data thats unique to each instance 
        self.fname=fname
        self.lname=lname
        self.age=age
        Student.number_of_students+=1
        
    def display_fullname(self):
        return f'{self.fname} {self.lname}'

    def display_student_location(self):
        return f'Our location is in {self.location}'

print(Student.number_of_students)

std1= Student("Lody","Mtui",27)
std2= Student("Lui","Mtui",23)
std3= Student("Paul","Pogba",26)

print(Student.number_of_students)

std2.location='Kenya'

print(Student.location)
print(std2.display_student_location())
print(std3.location)
print(std2.__dict__)

print(std1.grades)


# print(std1)
# print(std2)
# print(std3)

# std1.fname="Lody"
# std1.lname="Mtui"
# std1.age=27

# std2.fname="Lui"
# std2.lname="Mtui"
# std2.age=23

# std3.fname="Paul"
# std3.lname="Pogba"
# std3.age=26

print(std1.age)
print(std2.age)
print(std3.age)

print(std1.display_fullname())
print(std2.display_fullname())
print(std3.display_fullname())

# When calling using class, you must pass instance
# i.e. self in form of std1,std2,std3.....
print(Student.display_fullname(std1))
print(Student.display_fullname(std2))
print(Student.display_fullname(std3))