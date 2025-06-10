class Employee:
    a=1
    def show(self):
        print("the value of class method is",self.a)
o=Employee()
o.a=23 # this is will show the instance attribute not the class defined attribute 
o.show()

class Employee:
    a=1
    @classmethod #this is a decorator
    def show(cls): # instead of self we use cls
        print("the value of class method is",cls.a)
o=Employee()
o.a=23 # this is will show the instance attribute not the class defined attribute 
o.show()