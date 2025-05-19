def palindrome_checker(string):
    if string==string[::-1]:
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")

palindrome_checker("malayalam")