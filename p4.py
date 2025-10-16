Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> a=10
>>> b=20
>>> print("a>b is",a>b)
a>b is False
>>> print("a<b is",a<b)
a<b is True
>>> print("a=b is",a=b)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("a=b is",a=b)
TypeError: print() got an unexpected keyword argument 'a'
>>> print("a==b is",a==b)
a==b is False
>>> a=10.00
>>> b=20
>>> print("a<b is",a<b)
a<b is True
>>> print("a==b is",a==b)
a==b is False
>>> print("a<=b is",a<=b)
a<=b is True
>>> print("a<b is",a<b)
a<b is True
>>> a=10
>>> b=dhana
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    b=dhana
NameError: name 'dhana' is not defined
>>> b="dhana"
>>> a=10
>>> print("a<b is",a<b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print("a<b is",a<b)
TypeError: '<' not supported between instances of 'int' and 'str'
>>> if(False==False)
SyntaxError: expected ':'
>>> (False==False)
True
>>> a=10
>>> b=6
>>> print("a&b is",a&b)
a&b is 2
print("a|b is",a|b)
a|b is 14
print("a<<b is",a<<b)
a<<b is 640
print("a>>b is",a>>b)
a>>b is 0
print("a^b is",a^b)
a^b is 12
print("~b is",~b)
~b is -7
print("~a is",~a)
~a is -11
print("10<<2 is",10<<2)
10<<2 is 40
a=type(input)
a=10
a=type(a)
print(a)
<class 'int'>
a=input
a=input()
type(a)
x=10
y=10
print(x is y )
True
a=10
b=12
print(a is b)
False
print(a is not b)
True
a=10
b=10
print(a is not b)
False
