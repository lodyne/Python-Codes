class Person:
    # Class Variables
    default_full_name = "Wayne Rooney"
    age = 36

    # Constructor
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    # Regular/Instance method
    def description(self):
        return f"I am {self.firstname} {self.lastname}"

    
person1 = Person("Lui", "Mtui", 26)
person2 = Person("Lod", "Mtui", 30)


print(person1.firstname)
print(person2.firstname)

print(person1.lastname)
print(person2.lastname)

print(person1.description())
print(person2.description())