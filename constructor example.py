class student:

    def __init__(self,x,y,z):
      self.name=x
      self.rollno=y
      self.marks=z


    def display(self):
       print("student name:{}\n marks:{}".format(self.name,self.rollno,self.marks))


s1=student("dhana",204,90)
s1.display()
s2=student("teja",45,90)
s2.display()
