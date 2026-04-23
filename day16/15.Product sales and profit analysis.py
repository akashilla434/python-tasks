from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({'Product': products, 'Sales': sales, 'Profit': profit})

plt.subplot(231)
plt.plot(df['Sales'], marker='o')
plt.title('sales trend')

plt.subplot(232)
plt.bar(df['Product'], df['Sales'], width=0.4)
plt.title('product vs sales')

plt.subplot(233)
plt.pie(df['Sales'], labels=df['Product'], autopct='%1.1f%%')
plt.title('sales contribution')

plt.subplot(234)
plt.hist(df['Profit'], bins=3,rwidth=0.4)
plt.title('profit distribution')

plt.subplot(235)
plt.scatter(df['Sales'], df['Profit'])
plt.title('sales vs profit')
plt.grid(True)

plt.show()
