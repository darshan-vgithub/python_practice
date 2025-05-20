def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

operator=input("Enter the operator: ")
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if(operator== "+"):
    a=add(num1,num2)
    print(a)
elif(operator== "-"):
    s=sub(num1, num2)
    print(s)
elif(operator== "*"):
    m=mul(num1,num2)
    print(m)
elif(operator== "/"):
    d=div(num1,num2)
    print(d)
else:
    print("Invalid operator")