#check the string is palindrome or not
str=input("Enter the string: ")

str2=str[::-1]

if(str.lower()==str2.lower()):
    print(str,"is a palindrome")
else:
    print(str,"is not a palindrome")