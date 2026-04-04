class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class manager(employee):
    def display(self):
        print("name:", self.name)
        print("salary:",self.salary)

m1 = manager("rahul",60000)
m1.display()
