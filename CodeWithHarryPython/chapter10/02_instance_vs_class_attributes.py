class Employee:
    language="Python"
    salary=100000000


Darshan=Employee()
Darshan.language="C++"
print(Darshan.language,Darshan.salary)  # Instance attributes, take preference over class attributes during assignment & retrieval.