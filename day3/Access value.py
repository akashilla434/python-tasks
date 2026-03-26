Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> D={"A":70,"B":80,"C":100}
>>> print(d["A"])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(d["A"])
NameError: name 'd' is not defined. Did you mean: 'D'?
>>> print(D["A"])
70
