class Animal:
    def speak(self):
       return "some sound"
class Dog(Animal):
    def speak(self):
        return "woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"


animals=[Animal(),Dog(),Cat()]
for a in animals:
    print(a.speak())
