Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name=input("enter student name:")
enter student name:akash
>>> file=open("attendance.txt","a")
>>> file.write(name+"\n")
6
>>> file.close()
>>> file=open("attendance.txt","r")
>>> data=file.read()
>>> print("
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("\nAttendance Record")
...       

Attendance Record
>>> print(data)
...       
akash

>>> file.close()
...       
>>> 
>>> 
>>> 
>>> 
