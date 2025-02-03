# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

text=input("Enter the text: ")
if("Make a lot of money" == text):
    print("This is a spam")
elif("buy now" == text):
    print("This is a spam")
elif("subscribe this" == text):
    print("This is a spam")
elif("click this" == text):
    print("This is a spam")
else:
    print("This is not a spam")