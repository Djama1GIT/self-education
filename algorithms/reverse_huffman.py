amount, _ = map(int, input().split())
chars = {}
for i in range(amount):
    input_char = input().split(": ")
    chars[input_char[1]] = input_char[0]
output_which_is_input = input()
s = ""
for i in output_which_is_input:
    s += i
    if s in chars:
        print(chars[s], end="")
        s = ""