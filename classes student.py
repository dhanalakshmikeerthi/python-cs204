class student:
    __rollno=204
    __name="Dhana"
    def __display(self):
        print("rollno is:",self.__rollno)
        print("name is:",self.__name)
    def show(self):
        self.__display()
    
s1=student()
s1.show()  
