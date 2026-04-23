
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df=pd.DataFrame({'Students':students,'Marks':marks})

plt.subplot(231)
plt.plot(df['Students'],df['Marks'],marker='o')
plt.title('Trend of marks')

plt.subplot(232)
plt.bar(df['Students'],df['Marks'],color='green')
plt.title('Student vs Marks')

pass_count = np.count_nonzero(marks > 50)
fail_count = np.count_nonzero(marks <= 50)

data = [pass_count, fail_count]
labels = ['Pass', 'Fail']
colors = ['g', 'r']
explode = (0.1, 0)

plt.subplot(233)
plt.pie(data, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode)
plt.title('Pass (>50) vs Fail')

plt.subplot(234)
plt.hist(df['Marks'], bins=5, histtype='bar', rwidth=0.8, color='purple')
plt.title('Distribution of marks')

plt.subplot(235)
plt.scatter(df.index, df['Marks'], color='orange', s=100)
plt.title('Index vs marks')

plt.show()

