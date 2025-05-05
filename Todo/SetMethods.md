🔧 Adding & Removing Elements
Method	Description
set.add(elem)	Adds an element to the set
set.update(iterable)	Adds multiple elements from an iterable
set.remove(elem)	Removes an element (raises KeyError if not found)
set.discard(elem)	Removes an element (does not raise error if not found)
set.pop()	Removes and returns a random element
set.clear()	Removes all elements from the set

🔁 Set Operations (Mathematical)
Method	Description
set.union(other_set) or `set	other_set`
set.intersection(other_set) or set & other_set	Gets common elements
set.difference(other_set) or set - other_set	Gets elements in the first set but not in the second
set.symmetric_difference(other_set) or set ^ other_set	Gets elements in either set but not both
set.isdisjoint(other_set)	Returns True if no common elements
set.issubset(other_set)	Returns True if current set is a subset
set.issuperset(other_set)	Returns True if current set is a superset