def fib(n):
    if n<=0:
        return ("invalid")
    elif n==1 or n==2:
        return n-1
    else:
        a,b=0,1
    for _ in range(n-2):
        a,b=b,a+b
    return b
n=int(input("enter the number to find nth fib:"))
print("number :",fib(n))
    
    
 
