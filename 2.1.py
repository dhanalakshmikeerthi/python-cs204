class Car:  
    def __init__(self, make, model, year):
        self.make = make         
        self.model = model       
        self.year = year        
    def start(self):
        print(f"The {self.year} {self.make} {self.model} has started.")
    def stop(self):
        print(f"The {self.year} {self.make} {self.model} has stopped.")
car1 = Car("Tesla", "Model S", 2023)
car2 = Car("Audi", "Q8", 2025)
car1.start()  
car1.stop()   
car2.start()  
car2.stop()   
