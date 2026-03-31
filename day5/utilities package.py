Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from utilities import math_operations
... print("For Default values")
... print("Sum is ",math_operations.add(2,4))
... print("Multiplication is ",math_operations.mul(2,4))
... 
... from utilities import string_operations
... 
... print("Uppercase is ",string_operations.upper('abcd'))
... print("Character count is ",string_operations.counting("xyz"),'\n')
... 
... x=int(input("Enter a number "))
... y=int(input("Enter another number "))
... print("Sum is ",math_operations.add(x,y))
... print("Multiplication is ",math_operations.mul(x,y),'\n')
... 
... s=str(input("Enter only characters "))
... print("Uppercase is ",string_operations.upper(s))
... print("Character count is ",string_operations.counting(s),'\n')
SyntaxError: multiple statements found while compiling a single statement
>>> 
