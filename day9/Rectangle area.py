class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        result = self.length * self.width
        print("Area of Rectangle:", result)

r1 = Rectangle(5,3)
r1.area()
