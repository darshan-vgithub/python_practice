# How do you prevent a python print() function to print a new line at the end.

def print_without_newline(text):
    print(text, end="")

print_without_newline("Hello, World!")