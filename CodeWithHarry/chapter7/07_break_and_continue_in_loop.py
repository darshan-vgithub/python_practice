for i in range(101):
    if i==51:
        break # exit the loop right now 
    print(i)

    # break kills the loop but continue doesn't 
    # continue says do not kill the loop but dont execute the current iteration but execute the next iteration

for i in range(101):
    if i==51:
        print("entering continue")
        continue # skip the current iteration
    print(i)