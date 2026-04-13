import numpy as np
values=np.array([10,12,15,18,100,14,13])
std=np.std(values)
filtered=values[(values>=-34) & (values<=86)]
print(filtered)
