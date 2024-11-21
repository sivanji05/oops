'''
Inheritance
To aquare the properties from to one class to another class.


types of inheritance:


1. single inheritance                        (a) ->(b)

2. multiple inheritance                     (a,b)->(c)

3. hierarchical inhrtitance                   (a)->(b) (a)->(c)

4. multilevel inheritance                   [a] -> [b] -> [c]

5. hybrid heritance                         is a combination of two or more types of inheritance   


'''
# 1.single inheritance.

#   (a) ->(b)
'''
class person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)

# x=person("siva",23)
# x.display()

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear= year

    def welcome(self):
        print("welcome",self.lname,self.fname,"to the class of",self.graduationyear)

    
x=student("Nooli","sivanji",2024)
y=student("siva","nooli",2023)
x.welcome()
y.welcome()
#x.display()

'''

'''
class human:
    def __init__(self,heart):
         self.n_eyes=2
         self.n_noise=1
         self.heart=heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")

class Male(human):
    def __init__(self,name,heart):
        self.name=name
        super().__init__(heart)
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()
        print("i can code")
    def print_d(self):
        print(f"hi , iam {self.name} and i have {self.heart} heart")
    


m=Male("sivanji",5)
# m.eat()
# m.flirt()
#m.work()
#print(m.n_eyes)
print(m.name)
#print(m.heart)
m.print_d()
'''
#--------------------------------------------------------------

# 2.multipule inheritance 

'''
#  -> to aquare the proprties form muliplte super class
#    (a,b)->(c)

class human:
    def __init__(self,heart):
        print("calling form human")
        self.n_noise=1
        self.n_ears=2
        self.heart=heart

    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class male:
    def __init__(self,name):
        print("calling from male")
        self.name=name
    def flirt(self):
        print("i can flirt")
    def work(self):
        print("i can code")

class boy(human,male):
    def __init__(self,name,heart,lan):
        human.__init__(self,heart)
        male.__init__(self,name)
        self.lan=lan
    def sleep(self):
        print("i can sleep")

    def work(self):
        print("i can test")
    def print_d(self):
        print(f"hi , my name is {self.name}. i have {self.heart} heart and my heart wants {self.lan}.")


b=boy("sivanji",1,"python")
# print(b.n_noise)
# print(b.heart)
# print(b.lan)
b.print_d()

'''
#--------------------------------------------------------------

# 3.hierarchical inhrtitance
'''
# to aqure the propertiecs form one super to no of sub classes

class human:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print_d(self):
        print(self.name,self.age,self.gender)
    def eat(self):
        print("i can eat")

class male(human):
    def __init__(self, name, age,gender,salary):
        super().__init__(name,age,gender)
        self.salary=salary
    print("calling male class")
    def sleep(self):
        print("i can sleep")
    def print_d(self):
        print(f"my name is {self.name} and my age is {self.age}.my gender is {self.gender}. salary is {self.salary}")

class female(human):
    def __init__(self, name, age,gender,shopping):
        super().__init__(name, age,gender)
        self.shopping=shopping
    print("calling the female class")
    def work(self):
        print("i can work")
    def print_d(self):
        print(f"my name is {self.name} .my age is {self.age} and gender is {self.gender}.shopping interst {self.shopping}")


# f=female("mahi",22,"Female")
# print(f.name)
# m=male("sai",22,"Male")
# print(m.name)
# f.print_d()
# m.print_d()

m=male("sai",22,"Male","nill")
m.print_d()

f=female("mahi",22,"Female","Yes")
f.print_d()

f1=female("anitha",22,"Female","No")
f1.print_d()

'''
#--------------------------------------------------------------

#4. multilevel inheritance
'''
  #   [a] -> [b] -> [c]

class human:
    def __init__(self,n_heart):
        print("calling human class")
        self.n_heart=n_heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
    
class men(human):
    def __init__(self,name):
        print("calling men class")
        self.name=name
    def cook(self):
        print("i can cook")
class boy(men):
    def __init__(self,name,dance,n_heart,):
        human.__init__(self,n_heart)
        men.__init__(self,name)
        print("calling boy class")
        self.dance= dance
    def work(self):
        print("i can code")
    def print_d(self):
        print(f"my name is {self.name} and i have {self.n_heart} heart and i can dance = {self.dance}")

b=boy("sivanji","False",2)
b.print_d()
# # human.work(b)
# b.work()
'''

#--------------------------------------------------------------


#5. hybrid heritance
'''
#is a combination of two or more types of inheritance

class a:
    def dispaly(self):
        print("calling from class a")
class b(a):
    def dispaly(self):
        print("calling from class b")
class c:
    def dispaly(self):
        print("calling from class c")
class d(b,c):
    def dispaly(self):
        print("calling from class d")

d1=d()
d1.dispaly()
print(d.mro())

'''
#task on hybrid inheritance
'''
class university:
    def __init__(self,u_name):
        self.u_name=u_name
    def print_university(self):
        print(f"i am from {self.u_name}")

class course(university):
    def __init__(self,u_name,c_name):
        university.__init__(self,u_name)
        self.c_name=c_name
    def print_c_name(self):
        print(f"i am studying {self.c_name} in {self.u_name} ")

class branch(university):
    def __init__(self, u_name,b_name):
        university.__init__(self,u_name) 
        self.b_name=b_name
    def print_b_name(self):
        print(f"i am  studying {self.b_name} branch at {self.u_name}")

class faculty(branch):
    def __init__(self, u_name, b_name,f_name):
        branch.__init__(self,u_name, b_name)
        self.f_name=f_name
    def print_f_name(self):
        print(f"my name is {self.f_name} and i am teaching {self.b_name} in {self.u_name}")

class student(course,branch):
    def __init__(self,u_name,c_name,b_name,s_name):
        course.__init__(self,u_name,c_name)
        branch.__init__(self,u_name,b_name)
        self.s_name=s_name
    def print_s_name(self):
        print(f"my name is {self.s_name} and i am studying {self.c_name} in the {self.b_name} branch at {self.u_name}")



s = student("JNTUK", "AI", "CSE/AI", "sivanji")
s.print_s_name()

f=faculty("JNTUK","AI","SIVANJI")
f.print_f_name()

'''