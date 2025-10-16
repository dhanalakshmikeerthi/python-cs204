class student:
   def __init__(self,name,roll):
     self.name=name
     self.roll=roll
     

   def __eg__(self,other):
     return self.roll==other.roll

s1=student("Dhana",204)
s2=student("chandu",204)


print(s1 == s2)
