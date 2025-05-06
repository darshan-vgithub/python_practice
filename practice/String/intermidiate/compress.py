string="aaabccddd"
# output: a3b1c2d3

output=""
count=1
for i in range(1,len(string)):
    if(string[i]==string[i-1]):
        count+=1
    else:
        output=output+string[i-1]+str(count)
        count=1
output=output+string[i]+str(count)
print(output)