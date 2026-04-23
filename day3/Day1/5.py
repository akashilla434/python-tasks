Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=int(input("Enter number 1: "))
Enter number 1: 
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=int(input("Enter number 1: "))
ValueError: invalid literal for int() with base 10: ''
>>> b=int(input("enter number 2: "))
enter number 2: 
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b=int(input("enter number 2: "))
ValueError: invalid literal for int() with base 10: ''
>>> c=int(input("enter number 3: "))
enter number 3: 
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    c=int(input("enter number 3: "))
ValueError: invalid literal for int() with base 10: ''
>>> print("Average:", (a+b+c)/3)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("Average:", (a+b+c)/3)
NameError: name 'a' is not defined
