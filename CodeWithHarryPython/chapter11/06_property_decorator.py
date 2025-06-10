class Employee:
    a=1
    @classmethod #this is a decorator
    def show(cls): # instead of self we use cls
        print("the value of class method is",cls.a)


    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,name):
        self.fname=name.split(" ")[0]
        self.lname=name.split(" ")[1]
o=Employee()
o.a=23 # this is will show the instance attribute not the class defined attribute 
o.show()

o.name="Darshan Venkateshmurthy"
print(o.name)