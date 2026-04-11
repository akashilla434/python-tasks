import copy
a=[[101,"A"],[102,"B"],[103,"C"]]
b=copy.deepcopy(a)
b[0][0]=100
print(a)
print(b)
