import numpy as np
import pandas as pd
data = pd.DataFrame({
        "Name": ["A", "B", "C"], 
        "Math": [80, 70, 60], 
        "Science": [90, 60, 70]})
print(data)

data["Total"]=data["Math"]+data["Science"]
print(data)

high = data.loc[data["Total"].idxmax()]

print(high)
