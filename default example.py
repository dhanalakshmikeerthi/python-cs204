class Demo:
    def greet(self,name=None):
      if name:
        print(f"Hello,{name}!")
      else:
        print("Hello!")


obj = Demo()
obj.greet()
obj.greet("Dhana")
