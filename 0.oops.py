 # OOPS ->  object orianted programing language
'''
1. class             

2. object

3. Encapsulation  -> it is a concept of wrapping the data (variables) and code acting on the data (methods) together as a single unit.

4. Inheritance    ->  

5. Polymorphism 

6. Abstraction


'''


# Class 
'''
1. it is logical entity that contains some attributes and methods
2. class is blue print and it is a collection of objects.

syntax:
    class <name>:
        pass


class name:
    pass
    
'''

# Object
'''
1.The object is an real world entity that has a state and behavior associated with it. 

syntax :     obj = Dog()

'''
#example code for class and object
'''
class car:
    def __init__(self,modelname,price):

        self.modelname=modelname
        self.price=price

    def display(self):
        print(self.modelname,self.price)

c1=car("Toyota",200000)
c1.display()

'''
