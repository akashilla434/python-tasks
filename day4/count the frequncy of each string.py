Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> text=input("enter a string")
enter a stringpineapple
>>> freq={}
>>> for char in text:
...     if char in freq:
...         freq[char] +=1
...     else:
...         freq[char]=1
...     print("character frequency:")
...     for char in freq:
...         print(char, ":",freq[ch])
... 
...         
character frequency:
Traceback (most recent call last):
  File "<pyshell#10>", line 8, in <module>
    print(char, ":",freq[ch])
NameError: name 'ch' is not defined. Did you mean: 'chr'?
>>> print(char,":",freq[char])
p : 1
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
