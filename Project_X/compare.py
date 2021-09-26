# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:27:02 2020

@author: KRISHNA
"""
f=open("RSRCE/sbce.txt","r")
clctn=[]
for i in f:
    abc=i.split()
    cdf=[abc[0],abc[2].split("+")]
    clctn.append(cdf)
for i in clctn:
    #print("\n"+i[0])
    name=[]
    match=[]
    for j in clctn:
        ss=0
        for k in range(6):
            abc=float(i[1][k])
            cde=float(j[1][k])
            val=min(abc,cde)
            ss+=val
        name.append(j[0])
        match.append(ss)
    #for j in range(len(name)):
    #    print("Score "+name[j]+" :"+str(match[j]))
    best=match.index(max(match))
    del match[best]
    del name[best]
    best=match.index(max(match))
    print("Best match for "+i[0]+" is "+name[best]+" with a score of "+str(match[best]))