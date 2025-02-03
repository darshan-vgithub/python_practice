# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

text=input("Enter the text: ")
if("Make a lot of money" in text):
    print("This is a spam")
elif("buy now" in text):
    print("This is a spam")
elif("subscribe this" in text):
    print("This is a spam")
elif("click this" in text):
    print("This is a spam")
else:
    print("This is not a spam")