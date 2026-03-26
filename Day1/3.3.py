Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> area = 3.14 * r * r
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    area = 3.14 * r * r
NameError: name 'r' is not defined
>>> r=6
>>> area=3.14 *r *r
>>> print("Area+",area)
Area+ 113.03999999999999
