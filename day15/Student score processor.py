import math
#stores student names and marks in a list of tuples
#lst=[("akash",55),("rajesh",50),("rahul",100),("monu",90),("naveen",45)]
lst=[]
for i in range(5):
    name, marks=input(),int(input())
    lst.append((name, marks))
#Convert data into a dictionary
dit={}
names=[]
marks=[]
for j in lst:
    names.append(j[0])
    marks.append(j[1])
#Convert data into a dictionary
dit["name"]=names
dit["marks"]=marks
#Use a loop + condition to find students scoring above 50
fil_arr=[]
for i in dit["marks"]:
    if i>50:
        fil_arr.append(i)
print(fil_arr)
avg=math.fsum(fil_arr)/len(fil_arr)
print(avg)
with open("text.txt",'w') as file:
    file.write(f"Average marks of students: {avg}")
