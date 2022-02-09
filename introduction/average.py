school=[[0] for i in range(11)]
with open("file.txt") as klass:
    for i in klass:
        s=i.split()
        school[int(s[0])-1]+=[int(s[2])]
for i in range(len(school)):
    if sum(school[i]) == 0:
        print(i+1,"-")
    else:
        print(i+1, float(sum(school[i])/(len(school[i])-1)))