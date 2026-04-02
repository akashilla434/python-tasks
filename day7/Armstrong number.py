Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num = int(input("enter number:"))
enter number:153
>>> a = num % 10
>>> b = (num // 10)% 10
>>> c = num // 100
>>> sum = a*a*a* + b*b*b +
SyntaxError: invalid syntax
>>> sum = a*a*a + b*b*b + c*c*c
>>> if sum == num:
...     print("Armstrong number")
... else:
...     print("not Armstrong number")
... 
...     
Armstrong number
>>> 153
153
>>> 
