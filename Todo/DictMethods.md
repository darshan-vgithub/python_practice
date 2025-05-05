📥 Access & Update
Method	Description
dict.get(key, default)	Returns value for key, or default if not found
dict[key]	Accesses the value for key (raises error if not found)
dict[key] = value	Adds or updates key-value pair
dict.update(other_dict)	Updates dictionary with another dictionary or key-value pairs

❌ Remove Items
Method	Description
dict.pop(key, default)	Removes key and returns value; returns default if key not found
dict.popitem()	Removes and returns the last inserted key-value pair (Python 3.7+)
dict.clear()	Removes all items from the dictionary

🔍 Check or Get Info
Method	Description
key in dict	Returns True if key exists
len(dict)	Number of key-value pairs
dict.keys()	Returns a view of all keys
dict.values()	Returns a view of all values
dict.items()	Returns a view of key-value pairs (as tuples)