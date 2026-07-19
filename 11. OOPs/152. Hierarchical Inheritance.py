class Shape:
    def draw(self): print("Drawing shape")

class Square(Shape): pass
class Triangle(Shape): pass

s = Square()
t = Triangle()
s.draw()
t.draw()