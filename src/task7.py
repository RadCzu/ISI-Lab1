class Dog():
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def sound(self):
        print(f"{self.name} is barking!")


dog1 = Dog("burek", 5, "brown")
dog2 = Dog("reksio", 24, "white")
dog3 = Dog("kbkwefewfwe", 2, "gsgse")

dog1.sound()
dog2.sound()
dog3.sound()