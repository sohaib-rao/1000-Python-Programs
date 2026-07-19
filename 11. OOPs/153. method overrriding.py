class Bird:
    def speak(self):
        return "Chirp"

class Crow(Bird):
    def speak(self): 
        return "Caw Caw"

c = Crow()
print(c.speak()) 