from collections import deque
# Изучите эту программу и модифицируйте ее с использованием очереди deque вместо списка st.
# Кроме того, добавьте возможность выделения выражений в квадратных скобках.
#
# def get_sub_eq(eq_str):
#     st = []
#     res = []
#
#     for i, x in enumerate(eq_str):
#         if x == "(":
#             st.append(i)
#         elif x == ")":
#             res.append(eq_str[st.pop()+1: i])
#
#     return res
#
#
# s = "2 + 3 * (1 - 5 - (3 * x - 5)) + (a - b)"
# res = get_sub_eq(s)
#
# (Гарантируется, что скобочная последовательность верная)


def get_sub_eq(eq_str):
    st = deque([])
    res = []

    for i, x in enumerate(eq_str):
        if "[" == x or x == "(":
            st.append(i)
        elif "]" == x or x == ")":
            res.append(eq_str[st.pop() + 1: i])

    return res


s = "2 + 3 * [1 - 5 - (3 * x - 5)] + (a - b)"
res = get_sub_eq(s)
print(res)
