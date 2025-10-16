Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=list(range(0,10,2))
print(l)
[0, 2, 4, 6, 8]
print(type(l))
<class 'list'>
s="Learning python is very very easy!!!"
l=s.split()
print(l)
['Learning', 'python', 'is', 'very', 'very', 'easy!!!']
print(type(l))
<class 'list'>
n=[10,20,30,40]
print(n)
[10, 20, 30, 40]
n[1]=777
print(n)
[10, 777, 30, 40]
n[4]=77
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    n[4]=77
IndexError: list assignment index out of range
n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])
[3, 5, 7]
print(n[4::2])
[5, 7, 9]
print(n[3:7])
[4, 5, 6, 7]
print(n[8:2:-2])
[9, 7, 5]
print(n[4:100])
[5, 6, 7, 8, 9, 10]
n=[1,2,3,4,5,6,7,8,9,10]
l=0
while i<len(n):
    print(n[i])
...     i=i+1
...  n=[1,2,3,4,5,6,7,8,9,10]
... i=0
... while i<len(n):
...     print(n[i])
...     i=i+1
...     
SyntaxError: unindent does not match any outer indentation level
>>> while i<len(n):
...     print(n[i])
...     i=i+1
...  n=[1,2,3,4,5,6,7,8,9,10]
... i=0
... while i<len(n):
...     print(n[i])
...     i=i+1
...     
SyntaxError: unindent does not match any outer indentation level
>>> n=[1,2,3,4,5,6,7,8,9,10]
... i=0
... while i<len(n):
...     print(n[i])
...     i=i+1
...     
SyntaxError: multiple statements found while compiling a single statement
>>> n=[0,1,2,3,4,5,6,7,8,9,10]
... i=0
... while i<len(n):
...     print(n[i])
...     i=i+1
...     
SyntaxError: multiple statements found while compiling a single statement
>>> n=[0,1,2,3,4,5,6,7,8,9,10]
>>> 
============================================================================ RESTART: C:/python dhana/for.py ===========================================================================
0
1
2
3
4
5
6
7
8
9
10
