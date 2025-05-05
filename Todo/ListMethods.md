🔧 Modification Methods
Method	Description
list.append(x)	Adds x to the end of the list
list.insert(i, x)	Inserts x at index i
list.extend(iterable)	Appends all items from an iterable (e.g. another list)
list.remove(x)	Removes the first occurrence of x
list.pop([i])	Removes and returns item at index i (default last)
list.clear()	Removes all items (empties the list)

🔁 Reordering & Sorting
Method	Description
list.sort()	Sorts the list in place
sorted(list)	Returns a new sorted list (original unchanged)
list.reverse()	Reverses the list in place
reversed(list)	Returns a reverse iterator (not in-place)

🔍 Searching & Info
Method	Description
list.index(x)	Returns the first index of x
list.count(x)	Returns the number of times x appears
len(list)	Returns the number of items in the list
x in list	Checks if x is in the list

🔄 Copying
Method	Description
list.copy()	Returns a shallow copy of the list
list[:]	Also creates a shallow copy via slicing

🔁 Conversion
list(str) → Converts a string (or any iterable) into a list of elements

str.join(list) → Joins list elements into a string