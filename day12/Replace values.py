import numpy as np
values=[5,12,18,7,25,30]
arr=np.array(values)
arr[arr>15]=0
print(arr)
