class Employee:
    def __init__(self):
        print("constructor of employee")
    a=1

class Programmer(Employee):
    def __init__(self):
         print("constructor of programmer")
    b=2
class Manager(Programmer):
    def __init__(self):
        print("constructor of manager")
    c=3

a=Employee()
print(a.a)

b=Programmer()
print(b.a,b.b)

c=Manager()
print(c.a,c.b,c.c)
