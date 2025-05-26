class Employee:
    language="Python"
    salary=100000000

    def getInfo(self):
        print(f"the languahge is {self.language} and the salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")

# in class if we create a method then we have to pass self as an argument whether we use it or not it is compulsary
Darshan=Employee()
Darshan.getInfo()
Darshan.greet()
