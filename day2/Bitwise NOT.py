Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num=int(input("enter the number:"))
enter the number:32
>>> num=int(input("enter the number:"))
enter the number:43
>>> print("Bitwise NOT:",~NUM)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("Bitwise NOT:",~NUM)
NameError: name 'NUM' is not defined. Did you mean: 'num'?
>>> print("Bitwise NOT:", num)
Bitwise NOT: 43
