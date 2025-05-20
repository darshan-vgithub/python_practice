import os 
base_path=r"d:\FlameBack\Repos\python_practice\CodeWithHarryPython\chapter9"
file_pth=os.path.join(base_path,"file.txt")
f=open(file_pth)
# data=f.readlines()
# print(data)
# print(type(data))


# line1=f.readline()
# print(line1)
# print(type(line1))

# line2=f.readline()
# print(line2)
# print(type(line2))

# line3=f.readline()
# print(line3)
# print(type(line3))

# line4=f.readline()
# print(line4)
# print(type(line4))
line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()

