Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
def sum_marks(marks):
    if not marks:
        return 0
    return marks[0]+sum_marks(marks[1:])

def std_details():

    subjects=("Math", "Science", "English")
    student_names=set()
    std_marks={}

    while True:
        print("\n1. Add Student\n2. Display Students\n3. Calculate Average\n4. Exit")
        choice=input("Enter choice: ")

...         try:
...             if choice=='1':
...                 name=str(input("Enter student name: "))
...                 marks=[]
...                 for sub in subjects:
...                     marks.append(float(input(f"Enter marks for {sub}: ")))
...                 std_marks[name]=marks
...                 student_names.add(name)
... 
...             elif choice=='2':
...                 for name, m in std_marks.items():
...                     print(f"{name}: {m}")
... 
...             elif choice=='3':
...                 name=input("Enter student name: ")
...                 if name not in std_marks:
...                     raise NameError("Student not found!")
... 
...                 total=sum_marks(std_marks[name])
...                 avg=total / len(std_marks[name])
...                 print(f"Total: {total}, Average: {avg}")
... 
...             elif choice=='4':
...                 break
... 
...             else:
...                 print("Enter choice numbers only")
... 
...         except ValueError:
...             print("Error: Please enter Characters only.")
...         except ValueError:
...             print("Error: Please enter numbers only.")
...         except NameError as e:
...             print(f"Error: {e}")
...         except ZeroDivisionError:
...             print("Error: No marks found to calculate average.")
...         except TypeError:
...             print("Error: Incorrect data type encountered.")
... 
