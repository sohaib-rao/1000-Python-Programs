class Animal:
    def eat(self):
        print("Eating...")

class Cat(Animal):
    def meow(self):
        print("Meow!")

my_cat = Cat()
my_cat.eat()  
my_cat.meow() 