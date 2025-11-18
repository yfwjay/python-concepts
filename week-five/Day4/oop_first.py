# We will create a class Car with data(brand , year , model) and behaviours(start and stop) then create our objects.

class Car:
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year

        # We define the method start
    def start(self):
        move = print(f"A {self.year} {self.model} {self.brand} is driving.")
        return move
    
    # Define the method stop
    def stop(self):
        decelerate = print(f"A {self.year} {self.model} {self.brand} is stoping.")
        return decelerate
    
    # we now create an instance of a class = object

mercedes = Car("Mercedes" , "S-class" , "2023")

mercedes.start()
mercedes.stop()