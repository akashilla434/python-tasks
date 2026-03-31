Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
>>> import math
>>> secret = random.randint(1,50)
>>> for i in range(5):
...     print("correct")
...     break
... else:
...     diff=math.fabs(secret-guess)
...     print("you are", diff, "away")
... 
...     
correct
>>> print("number was:", secret)
number was: 24
>>> 
