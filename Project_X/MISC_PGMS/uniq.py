from googlesearch import search
import urllib
from bs4 import BeautifulSoup as Soup
import numpy as np
'''
import os
f=open("DAT/TRAIN.txt","r")
a=[]
for i in f:
    a.append(i)
a=np.array(a)
b=np.unique(a)

c=[]
for i in b:
    i=i.split()
    i=" ".join(i)
    c.append(i)

print("Original set:"+str(len(b)))

empty=[]
for file in os.listdir("ALL"):
    if file.endswith(".txt"):
        file=file.split(".")
        abc=file[0]
        abc=abc.split()
        abc=" ".join(abc)
        empty.append(abc)

print("\nCreated set:"+str(len(empty)))
print("\nDesired difference:"+str(len(b)-len(empty)))

diffar=np.setdiff1d(c,empty)
print(len(diffar))

abc=empty[0].split()
abc=" ".join(abc)

cd=b[0].split()
cd=" ".join(cd)

if abc==cd:
    print("Yes")

cbs=open("left.txt","w")
for i in diffar:
    cbs.write(i+"\n")
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
def check(label,c):
    new=[]
    new=label.split()
    s_ent=""
    for i in new:
        s_ent+='+'+i+' '
    for j in search(s_ent,stop=1):
        s_ent=j
    if  ("https://www.youtube.com/watch" or "https://www.facebook" or "https://www.instagram" or ".svg" or "gstatic" or "pinterest" or "twitter" or "cms") in s_ent:
        g=open("ADDON.txt","a+")
        g.write(label)
        c.append(label)
        print(c)
f=open("DAT/TRAIN.txt","r")
a=[]
for i in f:
    a.append(i)
a=np.array(a)
b=np.unique(a)
c=[]
count=0
for i in b:
    count+=1
    if count>1702:
        print(count)
        check(i,c)