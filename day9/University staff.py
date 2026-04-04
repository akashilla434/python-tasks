class staff:
    def __init__(self,name):
     self.name=name
class professor(staff):
    def show(self):
        print("professor:",self.name)
class labassistant(staff):
    def show(self):
        print("lab assistant:",self.name)
class administrator(staff):
    def show(self):
        print("administrator:",self.name)
p = professor("dr.akash")
l = labassistant("rahul")
a = administrator("teja")
p.show()
l.show()
a.show()
