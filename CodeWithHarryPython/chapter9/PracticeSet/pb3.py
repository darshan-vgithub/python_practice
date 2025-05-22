import os

def generateTables():
    base_path = os.path.dirname(os.path.abspath(__file__))
    tables_dir = os.path.join(base_path, "tables")
    os.makedirs(tables_dir, exist_ok=True)  # Ensure the directory exists

    for n in range(1, 21):  # From 1 to 20
        file_path = os.path.join(tables_dir, f"table_{n}.txt")
        with open(file_path, "w") as f:
            for i in range(1, 11):  # Each table from 1 to 10
                f.write(f"{n} x {i} = {n * i}\n")
generateTables()