from datetime import date


class Person:

    # Constructor
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

    @staticmethod
    def get_birthday(age: int) -> date:
        current_date = date.today().year
        birthday = current_date - age
        return f"The year I was born is {birthday}"


person = Person("Lui", "Mtui")
# print(person.get_birthday(27)) # Not recommended to call staticmethod using instance of the class
print(Person.get_birthday(27))
