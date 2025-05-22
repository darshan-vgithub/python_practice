import random
import os

def game():
    print("you are playing the game ....")
    score=random.randint(1,62)
    base_path=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(base_path,"hiscore.txt")
    with open(file_path) as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    if(score>hiscore):
        with open(file_path,"w") as f:
            f.write(str(score))
    print(f"your score is {score} and hiscore is {hiscore}")

game()

