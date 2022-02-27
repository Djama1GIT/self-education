from math import ceil


def find(arr, num, down, up):
    center = ceil((up+down)/2)
    if arr[up] == num:
        return up + 1
    elif arr[down] == num:
        return down + 1
    elif up == center:
        return -1
    elif arr[center] == num:
        return center + 1
    elif arr[center] > num:
        return find(arr, num, down, center)
    else:
        return find(arr, num, center, up)


amount_a, *A = map(int, input().split())
amount_b, *B = map(int, input().split())

for i in B:
    print(find(A, i, 0, len(A) - 1), end=" ")