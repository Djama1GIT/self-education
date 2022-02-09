x={}
with open("file.txt", "r") as file:
    s=[]
    f=[]
    for i in file:
        f+=i.lower().split()
    for i in f:
        if i in x:
            x[i] +=1
        else:
            x[i] = 1
ii=0
kk=""
for k,i in x.items():
    if i > ii:
        ii=i
        kk=k
    elif i == ii and k < kk:
        kk = k
print(kk,ii)