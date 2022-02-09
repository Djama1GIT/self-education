a,b,c,s=[],[],[],[]
with open("file.txt", "r", encoding='utf-8') as file:
    for i in file:
        s+=[i.strip().split(";")]
        a+=[int(s[-1][1])]
        b+=[int(s[-1][2])]
        c+=[int(s[-1][3])]
        print((int(s[-1][1])+int(s[-1][2])+int(s[-1][3]))/3)
print(sum(a)/len(a),sum(b)/len(b),sum(c)/len(c))