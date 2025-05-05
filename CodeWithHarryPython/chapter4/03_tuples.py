a=(1,2,3,4,5)
print(type(a))
a1=()
print(type(a1))

b=(1)
print(type(b)) # if we have only one element in tuple then it will be considered as integer without comma

b=(1,)
print(type(b)) # if we have only one element in tuple then it will be considered as tuple with comma

c=(1,"harry",True,12.5,None)
print(type(c))

#c[0]="rohan" # tuples are immutable we cannot change the value
