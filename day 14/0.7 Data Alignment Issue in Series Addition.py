import pandas as pd
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"]) 
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"]) 
s3=S1+S2
print(s3)

fr=s3.fillna(0)
print(fr)
