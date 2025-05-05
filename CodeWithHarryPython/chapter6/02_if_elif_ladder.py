a=int(input("Enter your age: "))

if(a>=18):
    print("you are above the consent")
    print("you can vote")
elif(a==0):
    print("you are a kid")
    print("you can't vote")
elif(a==12):
    print("you are a teenager")
    print("you can't vote")
else:
    print("you are below the consent")
    print("you can't vote")