
>>> num = int(input("enter number:"))
enter number:8
>>> temp = num
>>> sum = 0
>>> while temp > 0:
...      digit = temp % 10
...      fact = 1
...      i = 1
...      while i <= digit:
...          fact =fact * i
...          i = i + 1
...      sum = sum + fact
...      temp= temp // 10
...  if sum == num:

>>> if sum == num:
...     print("storng number")
... else:
...     print("not storng number")
... 
...     
not storng number
>>> 
