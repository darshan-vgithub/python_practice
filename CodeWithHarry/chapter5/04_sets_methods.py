# Set is a collection of non-repetitive elements.

# 1.
# Sets are unordered => Element’s order doesn’t matter
# 2.
# Sets are unindexed => Cannot access elements by index
# 3.
# There is no way to change items in sets.
# 4.
# Sets cannot contain duplicate values.
s={1,2,3,4}
s.add(23)
print(s, type(s))

# operations 

s1={1,2,3,4}
print(len(s1))


print(s1.remove(3))
print(s1)

# add(element)
# update(iterable)
# remove(element)
# discard(element)
# pop()
# clear()
# union(*others)
# intersection(*others)
# difference(*others)
# symmetric_difference(other)
# issubset(other)
# issuperset(other)
# isdisjoint(other)
# copy()