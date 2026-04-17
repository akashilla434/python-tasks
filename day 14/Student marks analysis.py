import numpy as np
import pandas as pd
arr=np.array([[80,90],
              [70,60],
              [85,95]])
df=pd.DataFrame(arr,columns=["math","science"])
print(df)
df["total"]=df["math"]+df["science"]
print(df)
high=df.loc[df["total"].idxmax()]
print(high)
