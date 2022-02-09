x=[]
for i in range(4):
    x+=[input()]
dict1={k:v for k,v in zip(x[0],x[1])}
dict2={k:v for k,v in zip(x[1],x[0])}
for i in x[2]:
    print(dict1[i], end="")
print()
for i in x[3]:
    print(dict2[i], end="")