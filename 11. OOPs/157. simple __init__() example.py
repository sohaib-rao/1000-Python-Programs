class Person:
    def __init__(self, name):
        self.name = name 

    def say_hello(self):
        print("Hello, my name is " + self.name)

ali = Person("Ali")
ali.say_hello() 