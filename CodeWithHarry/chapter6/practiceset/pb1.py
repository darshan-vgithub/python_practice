# Write a program to find the greatest of four numbers entered by the user.

a=int(input("Enter the number 1: "))
b=int(input("Enter the number 2: "))
c=int(input("Enter the number 3:"))
d=int(input("Enter the number 4:"))

if(a>b and a>c and a>d):
    print(a,"is the greatest number")
elif(b>a and b>c and b>d):
    print(b,"is the greatest number")
elif(c>a and c>b and c>d):
    print(c,"is the greatest number")
else:
    print(d,"is the greatest number")