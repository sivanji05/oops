# Encapsulation

# Enacpsulation is a process of binding or wrapping the data and methods into a single unite.

'''
class car:
    def __init__(self,model,price):
        self.model=model
        self.price=price
    def display(self):
        print(self.model,self.price)

c1= car("Toyota","30000")
c1.display() 
    '''

'''
class student:
    def __init__(self,name,age,rollno,department):
        self.name=name
        self._age=age
        self._rollno=rollno
        self.__department=department

    def __display(self):
        print(f"name is {self.name}  age {self._age} rollno {self._rollno}  and department is {self.__department}")

    def displaydetails(self):
        self.__display()

class branch(student):
    def show(self):
        print("rollno is ",self._rollno)
        #print("department is ",self.__department)

s1=student("sivanji",23,25,"AI")
s1.displaydetails()
print(s1._age)
#print(s1.__department)
s1._student__display()
s1.age=62
print(s1.age)


b1= branch("siva",34,12,"AI")
b1.show()

'''


class student:
    def __init__(self,name,age,rollno,department):
        self.name=name
        self._age=age
        self._rollno=rollno
        self.__department=department
    def get_department(self):
        return self.__department
    # def set_department(self,department):
    #     if department=="AI":
    #         print("student is belongs to Ai") 
    #     elif department=="Cse":
    #         print("student is belongs to Cse")
    #     else:
    #         print("student is not belongs to any branch")
    #     self.__department=department
        

    def __display(self):
        print(f"name is {self.name}  age {self._age} rollno {self._rollno}  and department is {self.__department}")

    def displaydetails(self):
        self.__display()

class branch(student):
    def show(self):
        print("rollno is ",self._rollno)
        print("department is ",self.__department)

s1=student("sivanji",23,25,"AI")
# s1.displaydetails()
# print(s1._age)
#s1._student__display()
#print(s1.get_department())
#s1.set_department("Cse")
print(s1.get_department())
# b=branch("sivanji",23,25,"AI")

# b.show()