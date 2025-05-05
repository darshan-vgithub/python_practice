student_grade=int(input("Enter your grade: "))

if student_grade<50:
    print("Your grade is: F")
elif student_grade >=50 and student_grade<=60:
    print("Your grade is: D")
elif(student_grade>=60 and student_grade<=70):
    print("Your grade is: C")
elif(student_grade>=70 and student_grade<=80):
    print("Your grade is: B")
elif(student_grade>=80 and student_grade<=90):
    print("Your grade is: A")
else:
    print("Your grade is: Ex")