import numpy as np
from numpy import random
x=random.rand(5)
print(x)

s=[]
for i in x:
    i=i*100
    if i>50:
        s.append(True)
    else:
        s.append(False)
fl=x[s]
print(np.sort(fl))    
