# Write a program which finds out whether a given name is present in a list or not.

names=["Darshan","Bubu","Baba","Dudu"]

name=input("Enter the name: ")
if(name in names):
    print("Name is present in the list")
else:
    print("Name is not present in the list")