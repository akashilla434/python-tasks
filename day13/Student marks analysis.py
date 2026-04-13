import numpy as np
marks=np.array([
                [70,80,90],
                [60,75,85],
                [50,65,70],
                [90,95,85],
                [40,55,60]
                ])
total_marks=np.sum(marks,axis=1)
avg=np.mean(total_marks)
above_avg_students=total_marks[total_marks>avg]
print("total marks:", total_marks)
print("class average:",avg)
print("above average students:", above_avg_students)
