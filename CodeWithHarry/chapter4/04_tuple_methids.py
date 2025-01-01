a=(1,2,2,3,45,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
no=a.count(2)
print(no)


i=a.index(20)
print(i)


# count()

# Description: Returns the number of times a specified value appears in the tuple.
# Usage: tuple.count(value)

# index()

# Description: Returns the index of the first occurrence of a specified value in the tuple. Raises a ValueError if the value is not found.
# Usage: tuple.index(value)
# Additional Tuple Features
# While tuples themselves have limited methods, you can use many built-in Python functions and operations with tuples:

# len(): Returns the length of the tuple.
# Example: len(tuple)
# max(): Returns the largest element in the tuple.
# Example: max(tuple)
# min(): Returns the smallest element in the tuple.
# Example: min(tuple)
# sum(): Returns the sum of the elements in the tuple (if all elements are numbers).
# Example: sum(tuple)
# sorted(): Returns a sorted list from the elements in the tuple.
# Example: sorted(tuple)
# Tuple-Specific Operations
# Accessing elements: tuple[index]
# Slicing: tuple[start:end:step]
# Concatenation: tuple1 + tuple2
# Repetition: tuple * n
# Membership testing: element in tuple
# Tuples are immutable, so they do not have methods that modify their contents (e.g., no append, remove, or pop methods like lists).