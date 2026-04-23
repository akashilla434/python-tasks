from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

df=pd.DataFrame({'Products':products,'Sales':sales})

plt.subplot(131)
plt.plot(df['Products'],df['Sales'])
plt.subplot(132)
plt.bar(df['Products'],df['Sales'])
plt.subplot(133)
#fig1,ax1=plt.subplots()
plt.pie(df['Sales'], labels=df['Products'],autopct='%1.f%%')
plt.suptitle('Visualization of 3 Charts')
plt.savefig('Visualization_of_3_Charts.png')
plt.show()
