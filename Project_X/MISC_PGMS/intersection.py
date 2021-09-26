import numpy as np
a,b=[],[]
f=open("actor.txt","r")
g=open("bus.txt","r")
for line in f:
    a.append(line)
for line in g:
    b.append(line)
c=np.intersect1d(a,b)
for i in c:
    print(i)