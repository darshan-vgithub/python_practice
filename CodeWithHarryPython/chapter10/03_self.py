class Employee:
    language="Python"
    salary=100000000



    def __init__(self):  #this is dunder method which is automatically called 
        #dunder method is a method which has __ before and after it
        print("I am a object")


    def getInfo(self):
        print(f"the languahge is {self.language} and the salary is {self.salary} and the name is {self.name}")
    @staticmethod
    def greet():
        print("Good morning")

# in class if we create a method then we have to pass self as an argument whether we use it or not it is compulsary
Darshan=Employee()
Darshan.name="lala"
Darshan.getInfo()
Darshan.greet()




print(".....................................this is a employee class.....................................")


class Person:
    age=22
    occupation="developer"

    def __init__(self, name, age, occupation):
        self.name=name
        self.age=age
        self.occupation=occupation
        print("Iam craeting a object")


rohan=Person("Darshan",22,"software developer")
print(rohan.name, rohan.age, rohan.occupation)