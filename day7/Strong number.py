Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num = int(input("enter number:"))
enter number:8
>>> temp = num
>>> sum = 0
>>> while temp > 0:
...      digit = temp % 10
...      fact = 1
...      i = 1
...      while i <= digit:
...          fact =fact * i
...          i = i + 1
...      sum = sum + fact
...      temp= temp // 10
...  if sum == num:
...      
SyntaxError: unindent does not match any outer indentation level
>>> if sum == num:
...     print("storng number")
... else:
...     print("not storng number")
... 
...     
not storng number
>>> 
