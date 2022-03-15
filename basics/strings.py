def first():
    s, a, b = input(), input(), input()
    i = 0
    if a in b and a in s:
        print("Impossible")
    else:
        while i < 1000:
            x = s.replace(a, b)
            if s == x:
                print(i)
                break
            s = x
            i += 1
        else:
            print("Impossible")


def second():
    x, i = 0, 0
    s, t = input(), input()
    while i < len(s) and t in s[i:]:
        x += 1
        i = s.find(t, i) + 1
    print(x)


def test():
    first()
    # second()


if __name__ == '__main__':
    test()