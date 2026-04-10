import numpy as np
sensor1 = [10,20,30]
sensor2 = [40,50,60]
sensor1=np.array(sensor1)
sensor2=np.array(sensor2)
combined=np.concatenate((sensor1,sensor2))
print("combined array:", combined)
