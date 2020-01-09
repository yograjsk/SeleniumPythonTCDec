class Animal:
    def speak(self):
        print("Speaking...")

class Dog(Animal):
    def Bark(self):
        print("Barking...")

class PuppyDog(Dog):
    def Eat(self):
        print("Eating...")

pd = PuppyDog()
pd.speak()
pd.Bark()
pd.Eat()

