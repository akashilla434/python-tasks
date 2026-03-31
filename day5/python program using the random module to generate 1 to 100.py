Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
>>> numbers = []
>>> for i in range(10):
...     num = random.randint(1,100)
...     numbers.append(num)
... 
...     
>>> print(numbers)
[85, 43, 29, 87, 40, 99, 1, 84, 16, 90]
