# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# n=int(input("Enter your number: "))
# print(f"The factorial of {n} is {factorial(n)}")


# guess the correct number

# def guess_number(attempts_left):
#     if attempts_left == 0:
#         print("Sorry, you've used all 3 attempts.")
#         return

#     n = int(input(f"Attempt {4 - attempts_left}/3 - Enter your number: "))
#     if n == 5:
#         print("Correct number!")
#         return
#     else:
#         print("Wrong number.")
#         guess_number(attempts_left - 1)

# # Start with 3 attempts
# guess_number(3)



def password_login(attempt_lest):
    if(attempt_lest == 0):
        print("Sorry, you've used all 3 attempts.")
        return
    print("Hi Welcome to password login")
    password=input(f"Attempt {4-attempt_lest}/3 - Enter the password: ")
    if(password=="darshan"):
        print("Correct password!")
        return
    else:
        print("Wrong password.")
        password_login(attempt_lest-1)

password_login(3)
