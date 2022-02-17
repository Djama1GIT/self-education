input_string, chars = input(), {}


def huf(ch):
    global out, s
    for last_num in range(len(ch)):
        s += str(last_num)
        if len(ch[last_num][0]) > 1:
            huf(ch[last_num][0])
        else:
            out[ch[last_num][0]] = s
        s = s[:-1]


for i in input_string:
    if i in chars:
        chars[i] += 1
    else:
        chars[i] = 1
chars = sorted([[k, v] for k, v in chars.items()], key=lambda index: index[1])

if len(chars) > 1:
    while len(chars) != 2:
        chars.append([[chars[0], chars[1]], chars.pop(0)[1] + chars.pop(0)[1]])
        chars = sorted(chars, key=lambda index: index[1])
    out = {}
    s, out_str = "", ""
    huf(chars)

    for i in input_string:
        out_str += out[i]

    print(len(out), len(out_str))
    [print(k, ": ", v, sep="") for k, v in out.items()]
    print(out_str)
elif input_string:
    print(1, len(input_string))
    print(input_string[0] + ":", 0)
    print("0" * len(input_string))