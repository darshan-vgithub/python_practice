def count_the_vowels(string):
    count=0
    for i in string:
        if i in "aeiouAEIOU":
            count+=1
    return count

string=input("Enter the string: ")
print(count_the_vowels(string))