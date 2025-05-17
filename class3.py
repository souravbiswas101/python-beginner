class Animal:
    def eat(self):
        print("The dog is eating.....\n")
    
class Mammal(Animal):
    def walk(self):
        print("The dog is walking.....\n")

class Dog(Mammal):
    def bark(self):
        print("The dog is barking......\n")


dog = Dog()
dog.eat()
dog.walk()
dog.bark()