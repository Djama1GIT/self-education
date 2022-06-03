def rearrange(str):
    str = str.split()
    arr = []
    for i in str:
        for c in i:
            if c.isnumeric():
                str[str.index(i)] = i[:i.index(c)] + i[i.index(c) + 1:]
                arr.append(int(c))
    xs = sorted(zip(str, arr), key=lambda tup: tup[1])
    return [x[0] for x in xs]


def maxPossible(integ, integer):
    arr = []
    for i in str(integer):
        arr.append(int(i))
    arr.sort(reverse=True)
    arr2 = []
    for i in str(integ):
        arr2.append(int(i))
    for i in arr2:
        for c in arr:
            if c > i:
                arr2[arr2.index(i)] = c
                del (arr[arr.index(c)])
                break
    return ''.join([str(i) for i in arr2])


def formula(form):
    boolean = True
    form = form.split("=")
    for i in range(len(form) - 1):
        if eval(form[i]) != eval(form[i + 1]):
            boolean = False
    return boolean


def test():
    print(*rearrange("is2 Thi1s T4est 3a"))
    print(maxPossible(9328, 456))
    print(maxPossible(523, 76))
    print(maxPossible(9132, 5564))
    print(maxPossible(8732, 91255))
    print(formula("6 * 4 = 24"))
    print(formula("18/17=2"))
    print(formula("16*10 = 160 = 14+ 120"))


if __name__ == '__main__':
    test()
