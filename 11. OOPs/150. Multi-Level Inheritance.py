class Organism:
    def live(self): print("Living")

class Mammal(Organism):
    def breathe(self): print("Breathing")

class Dog(Mammal):
    def bark(self): print("Barking")

d = Dog()
d.live()    
d.breathe() 
d.bark()