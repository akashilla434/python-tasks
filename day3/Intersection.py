Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={1,2,3,4}
>>> b={3,4,5,6]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> b={3,4,5,6}
>>> print(a.intersection(b))
{3, 4}
