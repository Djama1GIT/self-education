sets = []
for i in range(int(input())):
    a, b = map(int, input().split())
    sets.append([a, b])
sorted_sets = sorted(sets, key=lambda i: i[1])
points = [sorted_sets.pop(0)[1]]
while len(sorted_sets) != 0:
    while points[-1] in range(sorted_sets[0][0], sorted_sets[0][1] + 1):
        del(sorted_sets[0])
        if len(sorted_sets) == 0:
            break
    if sorted_sets:
        points += [sorted_sets.pop(0)[1]]
print(len(points))
print(*points)