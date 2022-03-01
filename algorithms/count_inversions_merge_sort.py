inversions = 0


def merge(arr_a, arr_b):
    global inversions
    len_a, len_b = len(arr_a), len(arr_b)
    a, b = 0, 0
    a2, b2 = 0, 0
    arr_final = []
    while a < len_a or b < len_b:
        if arr_a[a] > arr_b[b]:
            inversions += len_a - a
            b += 1
            if b == len_b:
                break
        else:
            a += 1
            if a == len_a:
                break
    while len_a > a2 and len_b > b2:
        if arr_a[a2] <= arr_b[b2]:
            arr_final += [arr_a[a2]]
            a2 += 1
        else:
            arr_final += [arr_b[b2]]
            b2 += 1
    else:
        return arr_final + (arr_a[a2:] if arr_a[a2:] else arr_b[b2:])


def mergesort(arr_a):
    len_a = len(arr_a)
    if len_a > 1:
        center = int(len_a / 2 + len_a % 2)
        return merge(mergesort(arr_a[:center]), mergesort(arr_a[center:]))
    else:
        return arr_a


input()  # only for stepik
arr = list(map(int, input().split()))

mergesort(arr)
print(inversions)