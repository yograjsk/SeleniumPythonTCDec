
class Animal:
    def speak(self):
        print("Speaking...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class DogPuppy(Dog):
    def eat(self):
        print("Eating...")

a = Animal()
a.speak()

d = Dog()
d.speak()
d.bark()

dp = DogPuppy()
dp.speak()
dp.bark()
dp.eat()