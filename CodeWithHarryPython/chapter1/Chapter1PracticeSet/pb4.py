# Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
import os

# Specify the directory you want to list
directory_path = '/'  # current directory, you can change it to any path

try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
