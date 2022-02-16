sets = [list(map(int, input().split())) for i in range(int(input()))]
points = []

for ps in sorted(sets, reverse=True):
    if not points or ps[1] < points[-1]:
        points.append(ps[0])

print(len(points))
print(*points)