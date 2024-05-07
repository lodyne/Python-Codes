class Person:
    default_full_name = "Wayne Rooney"
    age = 36

    # Constructor
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @classmethod
    def full_name(cls, name) -> str:
        cls.default_full_name = name
        return f"I am {cls.default_full_name}"

    # Class Method as Alternative Constructor
    @classmethod
    def from_string(cls, person_str: str):
        firstname, lastname, age = person_str.split("-")
        return cls(firstname, lastname, age)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


person1 = Person("Lui", "Mtui", 26)
person2 = Person("Lod", "Mtui", 30)

person_str1 = "Jesse-Lingard-29"
new_person1 = Person.from_string(person_str1)
print(new_person1)

print(new_person1.firstname)
print(new_person1.lastname)


# Person.full_name("Lod Mtui")
# person1.full_name("Lod Mtui")

print(Person.default_full_name)
print(person1.default_full_name)
print(person2.default_full_name)

print(person1.full_name("Lod Mtui"))
print(person2.full_name("Lui Mtui"))
