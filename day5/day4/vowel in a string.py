Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> text=input("enter a string")
enter a stringAIEOU
>>> count=0
>>> for char in text:
...     if char.lower() in"aeiou":
...         count+=1
...         print("number of vowels:",count)
... 
...         
number of vowels: 1
number of vowels: 2
number of vowels: 3
number of vowels: 4
number of vowels: 5
