class Dog:
    def sound(self):
        return "woof!"

class cat:
    def sound(self):
        return "meow!"
for animal in[Dog(),cat()]:
    print(animal.sound())
