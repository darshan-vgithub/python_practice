# Write a program to find the greatest of four numbers entered by the user.
a=int(input("Enter your number: "))
b=int(input("Enter your number: "))
c=int(input("Enter your number: "))
d=int(input("Enter your number: "))

if(a>b and a>c and a>d):
    print(a, "is greater")
elif(b>a and b>c and b>d):
    print(b , "is greater")
elif(c>a and c>b and c>d):
    print(c, "is greater")
else:
    print(d, "is greater")