class Animal:
    def speak(self):
        print("Speaking...")

class Dog(Animal):
    def speak(self):
        print("dog speaking...")

    def Bark(self):
        print("Barking...")

d = Dog()
d.speak()
d.Bark()
a = Animal()
a.speak()


'''
Class Base Class: Vehicle
Derived Classess: TwoWheeler, FourWheeler

'''