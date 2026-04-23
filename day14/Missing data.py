import numpy as np
import pandas as pd
arr=np.array([10,np.nan,30,np.nan,50])
s=pd.Series(arr)
print(s)
d = s.fillna(s.mean())
print(d)
