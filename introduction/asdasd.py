x={}
for i in range(int(input())):
    s=input().split(";")
    if not(s[0] in x):
        x[s[0]] = [0,0,0,0,0]
    if not(s[2] in x):
        x[s[2]] = [0,0,0,0,0]
    if int(s[1]) > int(s[3]):
        x[s[0]][1]+=1
        x[s[0]][4]+=3
        x[s[2]][3]+=1
    if int(s[1]) < int(s[3]):
        x[s[2]][1]+=1
        x[s[2]][4]+=3
        x[s[0]][3]+=1
    if int(s[1]) == int(s[3]):
        x[s[2]][2]+=1
        x[s[2]][4]+=1
        x[s[0]][4]+=1
        x[s[0]][2]+=1
    x[s[0]][0] += 1
    x[s[2]][0] += 1
for i,k in x.items():
    print(i+":",end="")
    print(*k)