from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df=pd.DataFrame({'Days':days,'Temprature':temps})
print(df)

plt.subplot(231)
plt.plot(df['Temprature'],marker='o')
plt.title('daily temperature trend')

plt.subplot(232)
plt.bar(df['Days'],df['Temprature'],width=0.4,color='r')
plt.title('day-wise temperature')

high_temps = df[df['Temprature'] > 30].count()['Temprature']
low_temps = df[df['Temprature'] <= 30].count()['Temprature']

labels = ['High (>30)', 'Low (≤30)']
sizes = [high_temps, low_temps]
colors = ['r', 'b']
plt.subplot(233)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
plt.title('proportion of high (>30) vs low temps')

plt.subplot(234)
plt.hist(df['Temprature'], bins=3, color='y', rwidth=0.4)
plt.title('temperature frequency')

plt.subplot(235)
plt.scatter(df.index, df['Temprature'], color='red', s=100)
plt.grid(True)
plt.title('day index vs temperature')

plt.show()

