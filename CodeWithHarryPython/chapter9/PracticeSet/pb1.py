# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

import os
def find_the_word_from_file():
    base_path=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(base_path,"poem.txt")
    f=open(file_path)
    data=f.read()
    if "twinkle" in data:
        print("Twinkle is present in the file")
    else:
        print("Twinkle is not present in the file")
    f.close()

find_the_word_from_file()
