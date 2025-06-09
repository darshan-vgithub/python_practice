class Employee:
    def __init__(self):
        print("this is a constructor")
class Programmer(Employee):
    def __init__(self):
        # super().__init__()
        print("this is a constructor of Programmer")

p=Programmer()