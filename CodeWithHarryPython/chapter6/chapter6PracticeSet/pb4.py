# Write a program which finds out whether a given name is present in a list or not.
username=input("Enter your username: ")

if len(username)<10:
    print(username,"it is less than 10 characters")
else:
    print(username,"it is greater than 10 characters")