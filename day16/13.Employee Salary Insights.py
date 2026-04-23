from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df=pd.DataFrame({'Department':departments,'Salary':salaries})

plt.figure('Employee Salary Insights')

plt.subplot(231)
plt.plot(df['Salary'],marker='o')
plt.title('Salary trend')

plt.subplot(232)
plt.bar(df['Department'],df['Salary'],width=0.4,color='r')
plt.title('Department-wise salary comparison')

dept_counts = df['Department'].value_counts()
plt.subplot(233)
plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%')
plt.title('Department distribution')

plt.subplot(234)
plt.hist(df['Salary'], bins=3, color='y', rwidth=0.4)
plt.title('Salary distribution')

plt.subplot(235)
plt.scatter(df.index,df['Salary'])
plt.grid(True)
plt.title('Index vs salary')

plt.show()
