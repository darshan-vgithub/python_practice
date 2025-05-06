string=input("Enter the string: ")
string2=input("Enter the string: ")

if(sorted(string)==sorted(string2)):
    print("Anagram")
else:
    print("Not Anagram")