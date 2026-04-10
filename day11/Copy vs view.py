import numpy as np
datasets=[10,20,30,40]
arr=np.array(datasets)
print("original array:",arr)
copy_arr=arr.copy()
arr[0]=99
print("modified original:",arr)
print("copy array:",copy_arr)
