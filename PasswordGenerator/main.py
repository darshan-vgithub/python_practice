import random , string

letters=string.ascii_letters
digits=string.digits
special_chars="!@#$%^&"
print("".join(random.choices(letters+digits+special_chars,k=8)))
