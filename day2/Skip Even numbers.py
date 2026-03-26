Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> for i in range (1,11)
SyntaxError: expected ':'
>>> for i in range(1,11):
...     if i %2==0:
...         continue
...     print(i)
... 
...     
1
3
5
7
9
