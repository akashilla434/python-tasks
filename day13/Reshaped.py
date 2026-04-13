import numpy as np
data=np.arange(1,13)
matrix=data.reshape(3,4)
print("marix:\n",matrix)
row_avg=np.mean(matrix,axis=1)
print("row_avg:",row_avg)
