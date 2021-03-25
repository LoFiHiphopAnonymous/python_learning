# practicing with object oriented programming

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.carOfChoice = None
    
    def get_Age(self, age):
        self.age = age

    def get_Name(self, name):
        self.name = name

    def share_Favorite_Car(self):
        #What if no car preference?
        if self.carOfChoice == None:
            print(f"My name is {self.name} and I walk everywhere and because of that I'm better than you.")
        #Car preference is known:
        else:
            print(f"My name is {self.name} and my favorite car to drive is a {self.carOfChoice}.")

class MercedesDriver(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.carOfChoice = 'Mercedes'
        

class TeslaDriver(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.carOfChoice = 'Tesla'

a = Person("Mark",18)
b = MercedesDriver("Amy",24)
c = TeslaDriver("Shadynasty",31)

print(type(a))
print(type(b))
print(type(c))

a.share_Favorite_Car()
b.share_Favorite_Car()
c.share_Favorite_Car()
