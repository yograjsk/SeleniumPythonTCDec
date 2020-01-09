
class Animal:
    def speak(self):
        print("Speaking...")

class Dog(Animal):
    def bark(self):
        print("Dog is Barking...")

a = Animal()
a.speak()

d = Dog()
d.speak()
d.bark()

