import numpy as np
matrix=np.random.randint(0,51,(3,3))
print("matrix:\n",matrix)
matrix=matrix[matrix>25]
print("values>25:",filter)
