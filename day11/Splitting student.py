import numpy as np
datasets=[50,60,70,80,90,100,110,120]
arr=np.array(datasets)
result=np.array_split(arr,4)
for i,part in enumerate(result):
    print(f"part{i+1}:",part)
