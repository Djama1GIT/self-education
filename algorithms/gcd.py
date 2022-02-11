def eugcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return eugcd(a % b, b)
    elif a <= b:
        return eugcd(a, b % a)


a, b = map(int, input().split())
print(eugcd(a, b))