str=input("Enter the String: ")

count=0
for i in str:
    if(i.lower()=='a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u'):
        count+=1
print(count)