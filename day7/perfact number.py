Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num=int(input("enter a number:"))
enter a number:6
>>> sum=0
>>> i=1
>>> while i<num:
...     if num%i==0:
...         sum = sum+1
...     i = i+1
... if sum==num:
...     
SyntaxError: invalid syntax
>>> if sum== num:
...     print("perfact number")
... else:
...     print("not perfact number")
... 
...     
not perfact number
