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

# Encapsulation


class university:
    def __init__(self,u_name):
        self.u_name=u_name
    def print_university(self):
        print(f"i am from {self.u_name}")

class course(university):
    def __init__(self,u_name,c_name):
        super().__init__(u_name)
        self.c_name=c_name
    def print_c_name(self):
        print(f"i am studying {self.c_name} in {self.u_name} ")

class branch(university):
    def __init__(self, u_name,b_name):
        super().__init__(u_name) 
        self.b_name=b_name
    def print_b_name(self):
        print(f"i am  studying {self.b_name} in {self.u_name}")

class faculty(branch):
    def __init__(self, u_name, b_name,f_name):
        super().__init__(u_name, b_name)
        self.name=f_name
    def print_f_name(self):
        print(f"my name is {self.name} and i am teaching {self.b_name} in {self.u_name}")

class student(course,branch):
    def __init__(self,u_name,c_name,b_name,s_name):
        super().__init__(self,u_name,c_name)
        branch.__init__(self,u_name,b_name)
        self.name=s_name

    def print_s_name(self):
        print(f"my name is {self.name} and i am studying {self.c_name} in {self.u_name} and {self.b_name}")


'''class student(course,branch):
    def __init__(self, u_name, c_name):
        super().__init__(u_name, c_name)


s = student("JNTUK", "AI", "CSE-AI", "SIVANJI")
course.print_c_name(s)
# f=faculty("JNTUK","AI","SIVANJI")
# f.print_f_name()
'''

