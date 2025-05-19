def fibbunaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbunaci(n-1) + fibbunaci(n-2)

n = int(input("Enter the number: "))
print(fibbunaci(n))
