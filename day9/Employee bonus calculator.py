def bonus_decorator(func):
    def wrapper(self):
        bonus = self.salary *0.10
        total_salary = self.salary + bonus
        print("salary with bonus:", total_salary)
    return wrapper
class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @bonus_decorator
    def display_salary(self):
        print("salary:", self.salary)
emp1 = employee("akash",100000)
emp1.display_salary()
