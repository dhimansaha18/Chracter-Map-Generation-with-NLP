import os
import wiki
c=0
for file in os.listdir("CLS/6/"):
    if file.endswith(".txt"):
        c+=1
        print(c)
        wiki.wiki("CLS/6/"+file)