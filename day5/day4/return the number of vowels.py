Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> text=input("enter a string:")
enter a string:hello akash
>>> vowel_count=0
>>> for char in text:
...     if char.lower() in "aieou":
...         vowel_count +=1
...         print("number of vowels in te string:"vowel_count)
...         
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("number of vowels in the string :", vowel_count)
number of vowels in the string : 0
>>> 
