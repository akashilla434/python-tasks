Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> str1=input("enter a first string")
enter a first stringakash
>>> str2=inpur("enter a second string")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    str2=inpur("enter a second string")
NameError: name 'inpur' is not defined. Did you mean: 'input'?
>>> str2=input("enter a second string")
enter a second stringilla
>>> output=str1+str2
>>> print("concatenated string is:",result)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("concatenated string is:",result)
NameError: name 'result' is not defined
>>> print("concatenated string is:",output)
concatenated string is: akashilla
