Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> file = open("notes.txt", "r")
>>> data + file.read()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    data + file.read()
NameError: name 'data' is not defined
>>> data = file.read()
>>> print(data)
day 1 pratice notes
python basics
>>> file.close()
>>> 
>>> 
