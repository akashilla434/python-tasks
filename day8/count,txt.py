Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> f=open("Article.txt","r")
... print(f.read(),'\n')
... 
... f=open("Article.txt","r")
... count=f.read()
... word=count.split()
... total_words=len(word)
... print("Words count is",total_words)
... f.close()
... 
... line=0
... f=open("Article.txt","r")
... for li in f:
...     line+=1
... print("Line count is",line)
... f.close()
... 
... f=open("Article.txt","r")
... char=f.read()
... total_char=len(char)
... print("Character count is",total_char)
... f.close()
SyntaxError: multiple statements found while compiling a single statement
