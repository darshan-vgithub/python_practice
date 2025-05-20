import os
st="Hey darshan  you are amazing and you are learning python"

base_path=r"d:\FlameBack\Repos\python_practice\CodeWithHarryPython\chapter9"
file_pth=os.path.join(base_path,"myfile.txt")
f=open(file_pth,"w")
f.write(st)
f.close()