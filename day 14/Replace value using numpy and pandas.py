import numpy as np
import pandas as pd
s=pd.Series([10,50,30,80,20])
print(s)
f1=pd.Series(np.where(s>40,0,s))
print(f1)
