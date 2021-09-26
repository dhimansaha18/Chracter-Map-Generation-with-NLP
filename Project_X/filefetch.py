import os
import numpy
def fetch(name):
    f=open("RSRCE/"+name+".txt","r",encoding="ISO-8859-1")
    ls=[]
    for i in f:
        i=i.lower()
        i=i.split()
        i=" ".join(i)
        ls.append(i)
    ls=numpy.unique(ls)
    fl=[]
    for file in os.listdir("BACKUP/ALL/"):
        if file.endswith(".txt"):
            a=file[:-4]
            a=a.lower()#new
            a=a.split()
            a=" ".join(a)
            fl.append(a)
    fl=numpy.array(fl)
    abc=numpy.intersect1d(fl,ls)
    X=[]
    for i in abc:
        fb=open("BACKUP/ALL/"+i+".txt","r",encoding="ISO-8859-1")
        X.append([i,fb])
    return X