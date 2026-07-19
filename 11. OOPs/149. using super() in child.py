class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand) 
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand, my_car.model)