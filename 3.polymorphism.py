#Polymorpsim
# poly means many and morphism means forms
#polymorphism means the same function name (but different signatures) being used for different types.


# python dosn't support method overloading.
# python support method overriding.

'''
polymorphism :
    1. duck typing               
    2. operator overloading     
    3. method overloading       
    4. method overriding        

    
'''


# duck typing
'''
class duck:
    
    def swim(self):
        print("i am duck and i can swim")
    
    def talk(self):
        print("quack quack")

class dog:
    def swim(self):
        print("i am dog and i can swim")

    def talk(self):
        print("bow bow")
class person:
    def talk(self):
        print("hello")

def display(obj):
    obj.swim()
    obj.talk()
    print("information dispalyed")


d=duck()
display(d)

dog=dog()
display(dog)

p=person()
display(p)

'''




#2. operator overloading 

'''class capmlex:
    def __init__(self,r,i):
        self.real=r
        self.imginary=i                    #----> getiing error because we are not able to add two objects

c1=capmlex(2,3)
c2=capmlex(4,5)
print(c1+c2)'''


# using magic methods we can add two objects
'''
class capmlex:
    def __init__(self,r,i):
        self.real=r
        self.imginary=i
    def __add__(self,other):
        return f"{self.real+other.real} + {self.imginary+other.imginary}i"
c1=capmlex(2,3)
c2=capmlex(4,5)
print(c1+c2)
        
'''


# check the greater number
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person("sivanji",21)
p2=person("siva",23)

if p1>p2:                                   #-> it's getting error because we are not able to compare two objects
    print("p1 is greterthan p2")
else:
    ("p2 is greterthan p1")
 '''


# using magic methods we can compare two objects
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __gt__(self,other):
        if self.age>other.age:
            print("p1 age is greterthan p2")

        else:
            print("p2 age is greterthan p1")

p1=person("sivanji",21)
p2=person("siva",23)
p1>p2

'''
               
#method overloading

# python dosn't support method overloading.

#1.example code for method overloading
'''
class student:
    def work(self):
        print("student is working")

    def work(self):
        print("student is playing")

s=student()
s.work()

'''


#2.example code for method overloading
'''
class leearning:
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c):
        return a+b+c
    
l=leearning()
print(l.add(2,3))
print(l.add(2,3,4))

'''

#method overriding
'''
class father:
    def sleep(self):
        print("father is sleeping")
    def work(self):
        print("father is working")
class son(father):
    def work(self):
        #print("son is working")
        super().work()

s=son()
s.work()
'''