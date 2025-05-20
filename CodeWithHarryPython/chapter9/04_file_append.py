import os
st="\nHello world"
base_path=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_path,"myfile.txt")
f=open(file_path,"a")
f.write(st)
f.close()