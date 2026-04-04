class student:
    def __init__(self,name,roll,marks):
         self.name = name
         self.roll = roll
         self.marks = marks
    def display(self):
         print("name:",self.name)
         print("roll number:", self.roll)
         print("marks:", self.marks)
         print("---------------------")

s1 = student("Rahul",1,85)
s2 = student("anith",2,98)
s3 = student("akash",3,89)

s1.display()
s2.display()
s3.display()







             
