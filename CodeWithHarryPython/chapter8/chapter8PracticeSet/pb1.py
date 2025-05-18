# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    return max(a,b,c)

a=int(input("Enter your number: "))
b=int(input("Enter your number: "))
c=int(input("Enter your number: "))

print(greatest(a,b,c))
