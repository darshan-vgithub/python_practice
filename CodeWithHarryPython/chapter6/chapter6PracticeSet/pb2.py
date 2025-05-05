# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1=int(input("Enter your marks: "))
sub2=int(input("Enter your marks: "))
sub3=int(input("Enter your marks: "))

if(sub1>33 and sub2>33 and sub3>33):
    if(sub1+sub2+sub3)/3>=40:
        print("You have passed")
    else:
        print("You have failed")
else:
    print("You have failed")