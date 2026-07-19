class Phone:
    def __init__(self):
        self.battery = 100
        
    def use_phone(self):
        self.battery = self.battery - 10 

my_phone = Phone()
print("Starting battery:", my_phone.battery)

my_phone.use_phone()
print("Battery after using:", my_phone.battery)