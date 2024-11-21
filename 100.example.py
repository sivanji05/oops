class University:
    def __init__(self, u_name):
        self.u_name = u_name

    def print_university(self):
        print(f"I am from {self.u_name}")


class Course(University):
    def __init__(self, u_name, c_name):
        University.__init__(self, u_name)
        self.c_name = c_name

    def print_course(self):
        print(f"I am studying {self.c_name} at {self.u_name}")


class Branch(University):
    def __init__(self, u_name, b_name):
        University.__init__(self, u_name)
        self.b_name = b_name

    def print_branch(self):
        print(f"I am in the {self.b_name} branch at {self.u_name}")


class Faculty(Branch):
    def __init__(self, u_name, b_name, f_name):
        Branch.__init__(self, u_name, b_name)
        self.f_name = f_name

    def print_faculty(self):
        print(f"My name is {self.f_name} and I am teaching in the {self.b_name} branch at {self.u_name}")


class Student(Course, Branch):
    def __init__(self, u_name, c_name, b_name, s_name):
        Course.__init__(self, u_name, c_name)
        Branch.__init__(self, u_name, b_name)
        self.s_name = s_name

    def print_student(self):
        print(f"My name is {self.s_name}. I am studying {self.c_name} in the {self.b_name} branch at {self.u_name}")


# Example usage:
s = Student("JNTUK", "AI", "CSE/AI", "sivanji")
s.print_student()

f = Faculty("JNTUK", "CSE/AI", "Dr. Sai")
f.print_faculty()




 

'''
 def add(a,b):
    return a+b

a,b=10,20
print(add(a,b))

class add:
    def add(self,a,b):
        return a+b
    
a=add()
#print(a.add(10,20))
 


def sub(d,f):
    return d-f

d,f=40,20
print(sub(d,f))


'''