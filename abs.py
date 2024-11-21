from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    @abstractmethod
    def printdetails(self):
        pass

    def start(self):
        print("Car is started")

    def accelerate(self):
        print("Car is accelerated")

    def brake(self):
        print("Car is stopped")

class Suv(Car):
    def printdetails(self):
        return f"Car brand {self.brand}, and model is {self.model}. Year of release {self.year} and price is {self.price} RS"
    
    def sunroof(self):
        print("Available")

class Bmw(Car):
    def printdetails(self):
        return f"Car brand {self.brand}, and model is {self.model}. Year of release {self.year} and price is {self.price} RS"
    
    def sunroof(self):
        print("Available")

# car1=suv("maruti","suzuki",2021,500000)
# print(car1.printdetails())

# car2=bmw("bmw","x1",2021,5000000)
# print(car2.printdetails())





# class bmw(car):
#     def __init__(self, brand, model, year, price):
#         super().__init__(brand, model, year, price)

#     def printdetails(self):
#         print(f" car brand {self.brand}, and model is {self.model}. year of realse {self.year} and price is {self.price}RS")

# car1=bmw("bmw","x1",2021,5000000)
# car1.printdetails()