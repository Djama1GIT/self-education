xyz=[0,0]
for i in range(int(input())):
    s=input().lower().split()
    if s[0] == "юг":
        xyz[1] -= int(s[1])
    elif s[0] == "север":
        xyz[1] += int(s[1])
    elif s[0] == "запад":
        xyz[0] -= int(s[1])
    elif s[0] == "восток":
        xyz[0] += int(s[1])
print(*xyz)