class Car:
    def __init__(self, name , fuel):
        self._name = name
        self.__fuel = fuel

    def start(self):
        print(f"The {self._name} with a fuel of {self.__fuel} is starting the journey!!")

class Lambo(Car):
    def feature(self):
        print(f"{self._name} has a Sunroof!!")

mercedes = Car("S-class" , "200L")
lambo = Lambo("Lamboghini" , "100L")
mercedes.start()
lambo.start()
lambo.feature()