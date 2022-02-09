x,s=set(),set()
for i in range(int(input())):
    s.add(input().lower())
for i in range(int(input())):
    xs=input().lower().split()
    for sx in xs:
        x.add(sx)
for i in x:
    if not (i in s):
        print(i)