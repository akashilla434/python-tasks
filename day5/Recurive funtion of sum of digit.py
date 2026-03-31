Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def sum(n):
...     if n == 0:
...         return 0
...     else:
...         return (n % 10) + sum(n // 10)
...     print("sum of a numbers:", sum(1234))
... 
...     
>>> print("sum of number:", sum(1234))
sum of number: 10
>>> 
>>> 
