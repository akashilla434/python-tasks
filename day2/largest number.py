Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=int(input(enter first:"))
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> a= int(input("enter first:"))
...             
enter first:10
>>> b=int(input("enter second :"))
...             
enter second :20
>>> c=int(input("enter third:"))
...             
enter third:15
>>> if a>=b and a>=c:
...             print("Largest:",a)
... elif b >=a and b >=c:
...     print("Largest:", b)
...     else:
...         
SyntaxError: invalid syntax
>>> else:
...     
SyntaxError: invalid syntax
>>> else c>=a and c<=b:
...     
SyntaxError: invalid syntax
>>> else:
...     
SyntaxError: invalid syntax
