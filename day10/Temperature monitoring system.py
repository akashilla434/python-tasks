import numpy as np
day1=[30,32,31]
day2=[29,33,34]
arr=np.array([day1,day2])
print(arr)
t=sum(arr)
print("day 1 temp is:",t[0])
print("day 2 temp is :",t[1])
print("total temp recorded is:",t.sum())
