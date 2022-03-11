#rofl
print(*str(__import__("datetime").date(*list(map(int, input().split()))) + __import__("datetime").timedelta(days=int(input()))).replace("-0", "-").split("-"))