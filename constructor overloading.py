class student:
    def __init__(self,name=None,age=None):
      if name and age:
          print(f"name: {name},Age: {age}")
      elif name:
          print(f"name: {name}")
      else:
          print("no details")
s1=student()
s2=student("Dhana")
s3=student("Sushu",19)
