from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df=df=pd.DataFrame({'Sales':sales,'Months':months})

plt.subplot(231)
plt.plot(df['Months'],df['Sales'],marker='o',color='b')
plt.title('Sales trend')
          
plt.subplot(232)
plt.bar(df['Months'],df['Sales'],color='c',width=0.7)
plt.title('Month-wise comparison')

plt.subplot(233)
plt.pie(df['Sales'],labels=df['Months'],autopct='%1.0f%%',)
plt.title('Contribution of each month')

plt.subplot(234)
plt.hist(df['Sales'], bins=5, color='m', rwidth=0.6)
plt.title('Frequency of sales values')

plt.subplot(235)
plt.scatter(df.index,df['Sales'],color='r',s=100)
plt.title('Month index vs sales')
plt.grid(True)
plt.show()
