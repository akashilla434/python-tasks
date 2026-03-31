Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import math
>>> num = float(input("enter a number: "))
enter a number: 80
>>> sqrt_val = mat.sqrt(num)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sqrt_val = mat.sqrt(num)
NameError: name 'mat' is not defined. Did you mean: 'math'?
>>> sqrt_val = math.sqrt(num)
>>> floor_val = math.floor(num)
>>> ceil_val = math.ceil(num)
>>> print("square root:',sqrt_val)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("square root:",sqrt_val)
...       
square root: 8.94427190999916
>>> print("floor valur:",floor_val)
...       
floor valur: 80
>>> print("ceiling value:",ceil_val)
...       
ceiling value: 80
>>> 
