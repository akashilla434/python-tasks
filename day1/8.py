Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=int(input("enter first number:6"))
enter first number:6
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=int(input("enter first number:6"))
ValueError: invalid literal for int() with base 10: ''
>>> a=int(input("enter first number: "))
enter first number: 4
>>> b-int(input("enter second number: "))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    b-int(input("enter second number: "))
NameError: name 'b' is not defined
>>> b=int(input("enter second number: "))
enter second number: 7
>>> print("product:",a*b)
product: 28
