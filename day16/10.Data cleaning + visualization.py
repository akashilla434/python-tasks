
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data = np.array([100, np.nan, 200, 150, np.nan, 300])
pds=pd.Series(data)
print(pds)
avg=pds.mean()
print(avg)
fpds=pds.fillna(avg)
print(fpds)

plt.plot(fpds,label="All Data",marker='o')

vgta=fpds[fpds>avg]

plt.bar(vgta.index, vgta, color='green', label='Above Average')
plt.axhline(avg, color='red', linestyle='--', label=f'Mean ({avg})')
plt.legend()
plt.savefig('Data_Cleaning_Visualization.png')
plt.show()




