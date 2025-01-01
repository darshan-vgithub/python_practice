marks=[]

f1=int(input("enter the first mark"))
f2=int(input("enter the second mark"))
f3=int(input("enter the third mark"))
f4=int(input("enter the fourth mark"))
f5=int(input("enter the fifth mark"))
f6=int(input("enter the sixth mark"))


marks.append(f1)
marks.append(f2)
marks.append(f3)
marks.append(f4)
marks.append(f5)
marks.append(f6)


sortedMarks=sorted(marks)
print(sortedMarks)