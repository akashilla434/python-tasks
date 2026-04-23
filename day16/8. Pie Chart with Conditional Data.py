import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
scores = np.array([40, 60, 80, 30, 90])
s=pd.Series(scores)
pass_count=(s>50).sum()
fail_count=(s<=50).sum()
labels=["pass","fail"]
values=[pass_count,fail_count]
print(values)
plt.pie(values,labels=labels,autopct='%1.1f%%',startangle=90)
plt.title("pass vs fail")
plt.show()
