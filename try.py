try:
    num = int(input("enter a number:"))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("invalid input!")
else:
    print("no exception")
finally:
    print("execution completed")
