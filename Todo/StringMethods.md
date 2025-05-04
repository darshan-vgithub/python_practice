str.lower()	Converts all characters to lowercase
str.upper()	Converts all characters to uppercase
str.capitalize()	Capitalizes the first letter
str.title()	Capitalizes the first letter of each word
str.swapcase()	Swaps uppercase to lowercase and vice versa
str.strip()	Removes leading and trailing whitespace
str.lstrip()	Removes leading whitespace
str.rstrip()	Removes trailing whitespace
str.replace(old, new)	Replaces substring old with new
str.removeprefix(prefix)	Removes a prefix (Python 3.9+)
str.removesuffix(suffix)	Removes a suffix (Python 3.9+)

str.find(sub)	Returns index of first occurrence or -1
str.index(sub)	Like find(), but raises error if not found
str.startswith(prefix)	Returns True if string starts with prefix
str.endswith(suffix)	Returns True if string ends with suffix`
str.count(sub)	Counts occurrences of substring

str.split(delim)	Splits string by delimiter into a list
str.rsplit(delim)	Splits from the right
str.partition(sep)	Splits into a 3-part tuple (before, sep, after)
'sep'.join(list)	Joins a list of strings with sep

str.isalpha()	Checks if all characters are alphabetic
str.isdigit()	Checks if all characters are digits
str.isalnum()	Checks if all characters are alphanumeric
str.isspace()	Checks if the string is all whitespace
str.islower() / str.isupper()	Checks character case