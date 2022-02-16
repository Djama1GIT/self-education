sets = []
for i in range(int(input())):
    a, b = map(int, input().split())
    sets.append([a, b])
sorted_sets = sorted(sets, reverse=True)
points = []
for ps in sorted_sets:
    if not points or ps[1] < points[-1]:
        points.append(ps[0])
print(len(points))
print(*points)