Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=20
>>> peint(a//b)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    peint(a//b)
NameError: name 'peint' is not defined. Did you mean: 'print'?
>>> a=20
>>> b=10
>>> print(a//b)
2
