x=""
with open("file.txt", "r") as file:
    s=[]
    vals=-1
    f=file.readline().strip()
    for i in f:
        if i.isnumeric():
            s[vals][1]=s[vals][1]*10+int(i)
        else:
            vals+=1
            s+=[[i,0]]
    for i in s:
        x+=i[0]*i[1]
with open("file.txt","w") as file:
    file.write(x)