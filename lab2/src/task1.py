from abc import ABC, abstractmethod
from typing import override


# czysto obiektowo, Animal powinno być abstrakcyjne bo sam obiekt "Animal" nie powinien wystąpić
class Animal(ABC):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @abstractmethod
    def sound(self):
        print("default sound")


class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    @override
    def sound(self):
        print("Woof woof")


class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    @override
    def sound(self):
        print("Meow")


class Fox(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    @override
    def sound(self):
        print("Ring-ding-ding-ding-dingeringeding")


dog = Dog("dog", 7, sex=True, breed="husky")

dog.sound()
print(dog.name)
print(dog.breed)
print(f"{dog.age}\n")

cat = Cat("cat", 3, sex=False, breed="orange")

cat.sound()
print(cat.name)
print(cat.breed)
print(f"{cat.age}\n")

fox = Fox("fox", 5, sex=False)

fox.sound()
print(fox.name)
print(fox.age)
gender = "female" if fox.age else "male"
print(gender)
