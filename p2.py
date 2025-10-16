Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=20
>>> c=a<b
>>> print(c)
True
>>> a=10
... b=20
... c=a>b
... print(c)
SyntaxError: multiple statements found while compiling a single statement
>>> c=a>b
>>> print(c)
False
>>> True+True
2
>>> True-True
0
>>> a="dhana"
>>> print(a)
dhana
>>> a="dhana'lakshmi"
>>> print(a)
dhana'lakshmi
>>> s1='''aditya
... college'''
>>> print(s1)
aditya
college
>>> a='dhana'lakshmi'
SyntaxError: unterminated string literal (detected at line 1)
>>> print(a)
dhana'lakshmi
>>> a="dhana"lakshmi'
SyntaxError: unterminated string literal (detected at line 1)
>>> print(a)
dhana'lakshmi
>>> a='hello'world'
SyntaxError: unterminated string literal (detected at line 1)
>>> print(a)
dhana'lakshmi
>>> name=input("enter your name:")
enter your name:dhana
>>> name=input("enter your name:")
enter your name:
>>> print("hello",world)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print("hello",world)
NameError: name 'world' is not defined

====================================================== RESTART: C:/Users/Dhana/AppData/Local/Programs/Python/Python313/python1.py ======================================================
enter your name:dhana
hello, dhana
