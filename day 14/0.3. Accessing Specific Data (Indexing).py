import pandas as pd
S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"]) 
print(S.loc[["B","D"]])

subset=S.loc[["B","D"]]
print(subset,type(subset))
