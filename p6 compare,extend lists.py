Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

======================== RESTART: C:/python dhana/if.py ========================
[0]
[0, 10]
[0, 10, 20]
[0, 10, 20, 30]
[0, 10, 20, 30, 40]
[0, 10, 20, 30, 40, 50]
[0, 10, 20, 30, 40, 50, 60]
[0, 10, 20, 30, 40, 50, 60, 70]
[0, 10, 20, 30, 40, 50, 60, 70, 80]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n=[1,2,3,4,5]
n.insert(1,888)
>>> print(n)
[1, 888, 2, 3, 4, 5]
>>> n=[1,2,3,4,5]
>>> n.insert(10,777)
>>> n.insert(-10,999)
>>> print(n)
[999, 1, 2, 3, 4, 5, 777]
>>> order1=["chicken","mutton","fish"]
>>> order2=["RC","KF","FO"]
>>> order1.extend(order2)
>>> print(order1)
['chicken', 'mutton', 'fish', 'RC', 'KF', 'FO']
>>> n=[10,20,30,40]
>>> print(n.pop())
40
>>> print(n.pop())
30
>>> print(n.pop())
20
>>> print(n.pop())
10
>>> print(n.pop())
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(n.pop())
IndexError: pop from empty list
>>> print(n)
[]
>>> x=[10,20,30,40]
>>> y=[1,2,3]
>>> z=x+y
>>> x+[10]
[10, 20, 30, 40, 10]
>>> a=[1,2,3]
>>> b=a*3
>>> print(b)
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> x=["Dog","Rat"]
>>> y=["Dog","Rat"]
>>> z=["DOG","RAT"]
>>> print(x==y)
True
>>> print(x==z)
False
>>> print(x!=z)
True
