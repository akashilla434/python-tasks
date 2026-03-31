Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def factorial (n):
...     if n == 0 or n == 1:
...          return 1
...     else:
...         return n * factorial(n-1)
... 
...     
>>> print(factorial(5))
120
