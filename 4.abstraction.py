# Abstraction 
'''

-Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of the object.

- python  bydefault  not support abstraction.

- wa can achive abstraction by using abstract Base class (ABC).


1. data abstraction
2. method abstraction
3. abstract class

'''

#1. data abstraction

from abc import ABC,abstractmethod

class car(ABC):
    def __init__(self,brand,model,year,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price

    @abstractmethod
    def printdetails(self):
        pass

    def start(self):
        print("car is started")

    def accelerate(self):
        print("car is accelerated")

    def brake(self):
        print("car is stopped")

class suv(car):
    # def printdetails(self):
    #     return f" car brand {self.brand}, and model is {self.model}. year of realse {self.year} and price is {self.price}RS"
    
    def sunroof(self):
        print("avaliabe")

class bmw(car):
    def printdetails(self):
        return f" car brand {self.brand}, and model is {self.model}. year of realse {self.year} and price is {self.price}RS"
    
    def sunroof(self):
        print("Not avaliabe")

car1=suv("maruti","suzuki",2021,500000)
print(car1.printdetails())
car1.start()

car1.accelerate()
car1.sunroof()



car2=bmw("bmw","x1",2021,5000000)
print(car2.printdetails())
car2.start()

car2.accelerate()
car2.sunroof()




# class bmw(car):
#     def __init__(self, brand, model, year, price):
#         super().__init__(brand, model, year, price)

#     def printdetails(self):
#         print(f" car brand {self.brand}, and model is {self.model}. year of realse {self.year} and price is {self.price}RS")

# car1=bmw("bmw","x1",2021,5000000)
# car1.printdetails()