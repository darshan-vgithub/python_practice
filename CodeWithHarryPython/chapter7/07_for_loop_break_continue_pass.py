# for i in range(1,100):
#     if(i==55):
#         break
#     print(i) # exit the loop right now 


for i in range(1, 100):
    if(i == 55):
        print("it is been skipped")
        continue # it will skip the current iteration
    print(i)


for i in range(1,100):
    pass # if you leave like this it will not give any error