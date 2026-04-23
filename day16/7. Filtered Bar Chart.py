from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

df=pd.DataFrame({'Marks':marks,'Names':names})

fil_df=df[df['Marks']>50]

plt.bar(fil_df['Names'],fil_df['Marks'],color='green')

plt.title('Students with Marks > 50')
plt.xlabel('Names')
plt.ylabel('Marks')
plt.savefig('Std_Mrks_Filtered_Bar_Chart.jpeg')
plt.show()
