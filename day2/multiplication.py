Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> number=int(input("enter number:"))
enter number:11
>>> for i in range(1,11):
...     print(num,"x",i,"=",num*i)
... 
...     
Traceback (most recent call last):
  File "<pyshell#3>", line 2, in <module>
    print(num,"x",i,"=",num*i)
NameError: name 'num' is not defined. Did you mean: 'sum'?
>>> 
>>> print('sum',"x",i,"=",'sum*i')
sum x 1 = sum*i
>>> 
