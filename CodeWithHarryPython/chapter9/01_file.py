import os
base_path = r"d:\FlameBack\Repos\python_practice\CodeWithHarryPython\chapter9"
file_path = os.path.join(base_path, "file.txt")
print(file_path)

f=open(file_path)
data=f.read()
print(data)

