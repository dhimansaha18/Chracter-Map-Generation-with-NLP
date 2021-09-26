def wiki(name):
    f=open("wiki_junk.txt","r")
    wik=[]
    for i in f:
        i=i.split()
        i=" ".join(i)
        wik.append(i)
    f.close()
    temp=[]
    f=open(name,"r")
    for j in f:
        j=j.split()
        j=" ".join(j)
        temp.append(j)
    for k in wik:
        while(True if k in temp else False):
            temp.remove(k)
    for k in temp:
        if "wikipedia articles " in k:
            temp.remove(k)
    f.close()
    f=open(name,"w")
    for m in temp:
        f.write(m+"\n")
    f.close()