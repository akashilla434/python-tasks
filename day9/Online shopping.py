class product:
    def __init__(self, name):
        self.name = name
class electronicproduct(product):
    def __init__(self,name,warranty):
        super().__init__(name)
        self.warranty = warranty
class mobilephone(electronicproduct):
    def display(self):
        print("product:",self.name)
        print("warranty:",self.warranty)
m = mobilephone("iphone:", "1 year")
m.display()
