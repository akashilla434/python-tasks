import random
import numpy as np
import pandas as pd
import math

# Student Class (OOP)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = self.assign_grade()

    def assign_grade(self):
        avg = sum(self.marks) / len(self.marks)

        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    def get_average(self):
        return sum(self.marks) / len(self.marks)


# Main Program
try:
    n = int(input("Enter number of students: "))

    students = []
    data = []

    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")

        # Generate random marks for 3 subjects (0–100)
        marks = [random.randint(0, 100) for _ in range(3)]

        # Store in NumPy array
        marks_array = np.array(marks)

        # Create Student object
        student = Student(name, marks_array)
        students.append(student)

        # Store data for DataFrame
        data.append([name, marks_array[0], marks_array[1], marks_array[2],
                     student.get_average(), student.grade])

    # Convert to Pandas DataFrame
    df = pd.DataFrame(data, columns=["Name", "Sub1", "Sub2", "Sub3", "Average", "Grade"])

    print("\n📊 Student Report:\n")
    print(df)

    # Math module (statistics)
    averages = df["Average"].values
    class_avg = sum(averages) / len(averages)
    std_dev = math.sqrt(sum((x - class_avg) ** 2 for x in averages) / len(averages))

    print("\n📈 Class Average:", class_avg)
    print("📉 Standard Deviation:", std_dev)

    # Save report to file
    df.to_csv("student_report.csv", index=False)
    print("\n💾 Report saved as student_report.csv")

except ValueError:
    print("❌ Invalid input! Please enter correct numbers.")
except Exception as e:
    print("⚠️ Error occurred:", e)
