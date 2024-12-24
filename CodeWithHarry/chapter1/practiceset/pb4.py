import os

def list_directory_contents(directory):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(directory)
        print(f"Contents of '{directory}':")
        
        # Iterate and print each item in the directory
        for item in contents:
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                print(f"File: {item}")
            elif os.path.isdir(item_path):
                print(f"Directory: {item}")
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory to list
directory_to_list = input("Enter the directory path: ")
list_directory_contents(directory_to_list)
