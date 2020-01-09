
class Animal:
    legs = 4
    def info(self):
        print("has four legs")



class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # self.name = name
        # self.age = age

    def DogInfo(self):
        print("this is dog")
        print(self.name)
        print(self.age)

myDog = Dog("Max", 15)
myDog.legs
# print(myDog.name)
# print(myDog.age)
myDog.DogInfo()




