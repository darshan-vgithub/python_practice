def prime_number(n):
    if n <= 1:
        return "Not prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not prime"
    return "Prime"


n = int(input("Enter the number: "))
print(prime_number(n))