Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> t=(1,2,3)
>>> l=list(t)
>>> l[0]=10
>>> t=tuple(1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t=tuple(1)
TypeError: 'int' object is not iterable
>>> print(t)
(1, 2, 3)
