class student(Exception):
    pass
def check_number(num):
    if num<0:
        raise student("Negative numbers are not allowed!")
    else:
        print("number is valid")
try:
    check_number(-10)
except student as e:
    print(f"Error:(e)")


    
