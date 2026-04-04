class vehicle:
    def __init__(self,brand, speed):
        self.brand=brand
        self.speed=speed
class car(vehicle):
    def display(self):
        print("car brand:",self.brand)
        print("speed:",self.speed)
class bike(vehicle):
    def display(self):
        print("bike brand:",self.brand)
        print("speed:",self.speed)
c1 = car("toyota",120)
b1 = bike("hero",120)
c1.display()
b1.display()
