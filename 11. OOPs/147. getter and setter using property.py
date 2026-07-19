class Temperature:
    def __init__(self, c):
        self._celsius = c

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible")
        self._celsius = value

temp = Temperature(25)
temp.celsius = 30 
print(temp.celsius)