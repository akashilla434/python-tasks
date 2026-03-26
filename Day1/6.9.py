Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> text="hello"
>>> print(f"{text:;<10}")
hello;;;;;
>>> print(f"{text:>10}")
     hello
>>> print(f"{text:^10}")
  hello   
