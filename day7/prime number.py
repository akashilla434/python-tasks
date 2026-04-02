Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num=int(input(" enter number:"))
 enter number:7
>>> count = 0
>>> i = 0
>>> while i <= num:
...     if num%i==0:
...         count = count + 1
...     i = i + 1
... if count == 2:
...     
SyntaxError: invalid syntax
>>> if count==2:
...     print("prime number")
... else:
...     print("not prime number")
... 
...     
not prime number
