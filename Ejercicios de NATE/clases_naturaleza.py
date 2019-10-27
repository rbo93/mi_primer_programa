
class Dog:
    def __init__(self, name, specie, age):
        self.name = name
        self.specie = specie
        self.age = age

    def speak(self):
        print("Guau guau")


my_dog1 = Dog("doggy", "Bulldog", 13)
my_dog2 = Dog("Goldencito", "Golden", 10)
my_dog3 = Dog("nigga", "Labrador", 5)


print(my_dog1.speak())
print(my_dog2.age)
print(my_dog3.specie)