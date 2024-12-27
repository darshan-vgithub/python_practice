name="Darshan"

print(len(name))
print(name.endswith("han"))
print(name.startswith("dar"))
print(name.capitalize())

"""
str.upper(): Converts the string to uppercase.
str.lower(): Converts the string to lowercase.
str.capitalize(): Capitalizes the first character of the string.
str.title(): Converts the first character of each word to uppercase.
str.strip(): Removes leading and trailing whitespace.
str.lstrip(): Removes leading (left) whitespace.
str.rstrip(): Removes trailing (right) whitespace.
str.replace(old, new): Replaces occurrences of old with new.
str.zfill(width): Pads the string with zeros on the left until it reaches the specified width.
2. Searching and Checking
str.find(sub): Returns the lowest index of the substring sub. Returns -1 if not found.
str.index(sub): Like find(), but raises a ValueError if the substring is not found.
str.startswith(prefix): Checks if the string starts with the specified prefix.
str.endswith(suffix): Checks if the string ends with the specified suffix.
str.count(sub): Counts the occurrences of a substring in the string.
3. Validation
str.isalpha(): Returns True if all characters are alphabetic.
str.isdigit(): Returns True if all characters are digits.
str.isalnum(): Returns True if all characters are alphanumeric (letters and numbers).
str.isspace(): Returns True if all characters are whitespace.
str.islower(): Returns True if all characters are lowercase.
str.isupper(): Returns True if all characters are uppercase.
str.istitle(): Returns True if the string is title-cased.
4. Splitting and Joining
str.split(delimiter): Splits the string into a list using delimiter. Default is whitespace.
str.rsplit(delimiter): Splits the string from the right into a list using delimiter.
str.splitlines(): Splits the string into a list at line breaks.
str.join(iterable): Joins elements of an iterable (e.g., list) into a string, using the string as a separator.
5. Formatting
str.format(*args, **kwargs): Formats the string with placeholders.
str.center(width): Centers the string, padding it with spaces or specified characters.
str.ljust(width): Left-aligns the string, padding with spaces or specified characters.
str.rjust(width): Right-aligns the string, padding with spaces or specified characters.
6. Encoding and Decoding
str.encode(encoding): Encodes the string into bytes using the specified encoding.
bytes.decode(encoding): Decodes bytes back into a string using the specified encoding.
7. Miscellaneous
str.len(): Returns the length of the string (actually len(str)).
str.partition(sep): Splits the string into a tuple: (before separator, separator, after separator).
str.rpartition(sep): Like partition(), but starts searching from the right.
str.casefold(): Converts the string to lowercase in a way that's more aggressive and suitable for caseless matching (used for case-insensitive comparisons).
"""