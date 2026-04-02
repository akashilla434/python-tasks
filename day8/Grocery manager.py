Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> items=input("enter items:")
enter items:soaps
>>> words=items.split()
>>> f=open("Grocery.txt","a")
>>> for word in words:
...     f.write(word + '\n')
... 
...     
6
>>> f=open("Grocery.txt","r")
>>> print("items are",'\n',f.read())
items are 
 soaps

>>> f.close()
>>> 
>>> 
>>> 
