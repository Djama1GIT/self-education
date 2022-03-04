inversions = 0


def merge(arr_a, arr_b):
    global inversions
    arr_final = []
    while arr_a and arr_b:
        if arr_a[0] <= arr_b[0]:
            arr_final += [arr_a.pop(0)]
        else:
            arr_final += [arr_b.pop(0)]
            inversions += len(arr_a)
    else:
        return arr_final + (arr_a or arr_b)


def mergesort(arr_a):
    len_a = len(arr_a)
    if len_a > 1:
        center = int(len_a / 2 + len_a % 2)
        return merge(mergesort(arr_a[:center]), mergesort(arr_a[center:]))
    else:
        return arr_a


arr = list(map(int, input().split()))

mergesort(arr)
print(inversions)