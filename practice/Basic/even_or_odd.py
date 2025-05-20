def even_or_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"


num = int(input("Enter a number: "))
print(even_or_odd(num))