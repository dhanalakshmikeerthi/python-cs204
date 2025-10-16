class student:
  def _init_(self,name,roll_no):
    self.name=name
    self.roll_no=roll_no
    print("inside constructor:")
    print("name:",self.name)
    print("roll_no:",self.roll_no)

  def update_marks(self,marks):
    self.marks=marks
    print("\ninside instance method:")
    print("\(self.name)'s marks updated to:",self.marks)

s1=student("dhana",204)
print("outside of class:")
print("name(before):",s1.name)

s1.name="dhana"
print("name(after):",s1.name)
s1.update_marks(99)
print("marks(outside):",s1.marks)
