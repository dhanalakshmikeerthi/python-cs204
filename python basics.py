Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=2
type(a)
<class 'int'>
a=0b100
print(a)
4
a=0o456
print(a)
302
a=0xfad
print(a)
4013
a=10.00
type(a)
<class 'float'>
a=0o123.45
SyntaxError: invalid syntax
>>> a=0b11+7j
>>> print(a)
(3+7j)
>>> a=3+0b11
>>> print(a)
6
>>> a=true
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> type(a)
<class 'int'>
>>> a=TRUE
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a=TRUE
NameError: name 'TRUE' is not defined. Did you mean: 'True'?
>>> print(a)
6
>>> a=Type
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a=Type
NameError: name 'Type' is not defined. Did you mean: 'type'?
>>> print(a)
6
>>> b=True
>>> print(b)
True
>>> b=type
>>> type(b)
<class 'type'>
>>> a=true
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> type(a)
<class 'int'>
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
