# Write a program to accept marks of 6 students and display them in a sorted manner.
student1=int(input("Enter your marks: "))
student2=int(input("Enter your marks: "))
student3=int(input("Enter your marks: "))
student4=int(input("Enter your marks: "))
student5=int(input("Enter your marks: "))   
student6=int(input("Enter your marks: "))
marks=[student1,student2,student3,student4,student5,student6]
marks.sort()
print(marks)