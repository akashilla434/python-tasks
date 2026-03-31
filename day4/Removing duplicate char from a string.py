Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> string=input("enter astring")
enter astringbanana
>>> result="'
SyntaxError: unterminated string literal (detected at line 1)
>>> result=""
>>> for ch in string:
...     if ch not in result:
...         result=result+ch
...         print("string after removing duplicates:",result)
... 
...         
string after removing duplicates: b
string after removing duplicates: ba
string after removing duplicates: ban
>>> 
