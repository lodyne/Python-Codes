class Person:
    default_full_name = "Wayne Rooney"
    age = 36

    # Constructor
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    # Regular method with property method
    @property
    def describe_me(self):
        return f"I am {self.firstname} {self.lastname}, and I am {self.age} years old."
        

person = Person("Lui", "Mtui", 27)
print(person.describe_me)