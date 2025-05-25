class Employee:
    name="Darshan"
    age=25
    language="Python"
    salary=100000

Darshan=Employee()
print(Darshan.name)
print(Darshan.age)
print(Darshan.language)
print(Darshan.salary)  # this is a object 


# class is a blueprint
print(".............................this is a persons class.....................................")
class Person:
    age=22
    occupation="student"
    degree="Btech"
    course="Computer Science"  # these are the class attributes which are common for all the objects

Darshan=Person()
print(Darshan.age)
Darshan.name="Darshan"  # here name is the object attribute and occupation , degree and course are the class attributes
print(Darshan.name)
print(Darshan.occupation)
print(Darshan.degree)
print(Darshan.course)