def LISBottomUp(arr):
    len_arr = len(arr)
    d_max = [0]*len_arr
    for i in range(len_arr):
        d_max[i] = 1
        for j in range(i):
            if arr[j] >= arr[i] and d_max[j] + 1 > d_max[i]:
                d_max[i] = d_max[j] + 1
    ans = max(d_max)

    print(ans)
    s = []
    prev = 0
    while ans > 0:
        this = d_max[::-1].index(ans, prev)
        s.insert(0, len_arr - d_max[::-1].index(ans, prev))
        prev = this
        ans -= 1
    print(*s)


input()  # Only for Stepik
LISBottomUp(list(map(int, input().split())))
