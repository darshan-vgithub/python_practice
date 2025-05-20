def factorical(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorical(n-1)

n=int(input("Enter the number: "))
print(factorical(n))