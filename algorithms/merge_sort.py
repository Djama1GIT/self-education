def merge(arr_a, arr_b):
    arr_final = []
    while arr_a and arr_b:
        arr_final += [arr_a.pop(0)] if arr_a[0] <= arr_b[0] else [arr_b.pop(0)]
    else:
        return arr_final + (arr_a if arr_a else arr_b)


def mergesort(arr_a):
    len_a = len(arr_a)
    if len_a > 1:
        center = int(len_a / 2 + len_a % 2)
        return merge(mergesort(arr_a[:center]), mergesort(arr_a[center:]))
    else:
        return arr_a


# input()
arr = list(map(int, input().split()))

print(mergesort(arr))
