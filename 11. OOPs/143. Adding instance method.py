class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

c = Circle(5)
print(c.calculate_area()) 