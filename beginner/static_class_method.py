from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birthday(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person('trinhlk2', 16)
person2 = Person.from_birthday('trinhlk3', 1992)
print(person1.age)
print(person2.age)
print(Person.is_adult(22))
