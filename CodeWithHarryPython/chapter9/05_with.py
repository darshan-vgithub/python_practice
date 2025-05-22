import os

base_path=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_path,"file.txt")
f=open(file_path)
data=f.read()
print(data)
f.close()

# this same thing can be done using the with block
with open(file_path) as f:
    data=f.read()
    print(data)

# and with this we dont even have to close the file