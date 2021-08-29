#The class Person which is a blueprint/template for my objects to store information about humans
class Person:

    #Class attribute -> constant, visible to all objects of the class
    MAX_ENERGY = 20

    #Static method -> Utility function, that does not require an object to exist
    @staticmethod
    def is_mature(age):
        if age >= 18:
            return True
        else:
            return False

    #Initialiser/Constructor function, invoked automatically when creating new objects of this class
    def __init__(self, name = "", age = 1, weight = 5, energy = 100):
        #These are instance attributes (what each item will have)
        self.name = name
        self.age = age
        self.weight = weight
        if energy > Person.MAX_ENERGY:
            self.energy = Person.MAX_ENERGY
        else:
            self.energy = energy
    
    #Instance method that works on each object of this class
    def hello(self):
        print(f"Details of a person:\nName: {self.name}\nAge: {self.age}\nWeight:{self.weight}\nEnergy:{self.energy}\n")
    
    def grow(self, years):
        self.age += years
    
    def eat(self, food, w):
        self.weight += w
        print(f"{self.name} have eated {food} and now weights {self.weight}")


p1 = Person()
p2 = Person("Octavian", 20, 68, 99)
p3 = Person("Tadek", 19, 55, 823828483647)

p1.name = "Peter"

if __name__ == "__main__":
    p2.hello()
    p2.grow(5)
    p2.hello()
    p2.grow(22)
    p2.hello()
    p2.eat("Cake", 0.4)
    p2.hello()
    p3.hello()
    p3.eat("Lasagne", 2)
    p3.hello()
    print(f"{Person.is_mature(50)}")
    print(f"{Person.is_mature(11)}")
    print(f"{Person.is_mature(p3.age)}")