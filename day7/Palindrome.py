Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num = int(input("enter number:"))
enter number:121
>>> temp = num
>>> rev = 0
>>> while temp > 0:
...     digit = temp % 10
...     rev = rev * 10 + digit
...     temp = temp // 10
... if rev == num:
...     
SyntaxError: invalid syntax
>>> if rev== num:
...     print("palindrome")
... else:
...     print("not palindrome")
... 
...     
not palindrome
