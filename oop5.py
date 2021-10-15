class User:
    firstname=''
    lastname=''

    #constructor
    def __init__(self,firstname,lastname):                    
        self.firstname=firstname
        self.lastname=lastname
    
    #function  inside the class must contain "self"  parameter
    def username(self):                                        
        return f'My name is {self.firstname} {self.lastname}.'

class Birthdate:
    day=20
    month=10
    year=1993

    def my_birthday(self):
        print(f"My birthday is {self.day}/{self.month}/{self.year}")

class Address:
    street="East Zoo"
    city="Dodoma"
    country="Tanzania"

    def where_i_live(self):
        print(f'Currently i live in {self.street},{self.city},{self.country}')

class Info:
    hobby="football"
    study="Bsc.SE"
    fanOf="Man United"

    def other_info(self):
        print(f'I am {self.hobby} fan of {self.fanOf} and i study {self.study}')

class Main:
    obj1=User('Lody','Mtui')
    print(obj1.username())

    obj2=Birthdate()
    obj2.my_birthday()

    obj3=Address()
    obj3.where_i_live()
    
    obj4=Info()
    obj4.other_info()