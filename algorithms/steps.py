_, x = input(), [0, 0] + list(map(int, input().split()))
for i in range(2, len(x)): x[i] += max(x[i - 1], x[i - 2])
print(x[-1])