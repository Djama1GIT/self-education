amount, capacity = map(int, input().split())
objects = []
backpack = 0

for i in range(amount):
    objects.append(list(map(int, input().split())))
    objects[-1].append(objects[-1][0] / objects[-1][1])
objects.sort(key=lambda i: i[2], reverse=True)

while capacity > 0 and amount:
    if objects[0][1] <= capacity:
        capacity -= objects[0][1]
        amount-=1
        backpack+=objects.pop(0)[0]
    else:
        backpack+=(objects[0][0]/objects[0][1])*capacity
        capacity = 0
print(f"{backpack:.3f}")