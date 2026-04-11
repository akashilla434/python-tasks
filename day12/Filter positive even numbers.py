import numpy as np
arr=[-5,10,15,-2,20,25,30]
np_arr=np.array(arr)
print(np_arr)
result=np_arr[(np_arr >0) & (np_arr % 2==0)]
print(result)

