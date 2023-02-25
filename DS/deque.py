from collections import deque
import sys
# dq = deque([1, 2, 3, 4, 5], maxlen=5)  # deque([1, 2, 3, 4, 5], maxlen=5) O(n)
# dq.append(6)  # deque([2, 3, 4, 5, 6], maxlen=5) O(1)
# dq.appendleft(1)  # deque([1, 2, 3, 4, 5], maxlen=5) O(1)
# dq.pop()  # returned 5; deque([1, 2, 3, 4], maxlen=5) O(1)
# dq.popleft()  # returned 1; deque([2, 3, 4], maxlen=5) O(1)
# dq.extend([5, 6, 7, 8])  # deque([4, 5, 6, 7, 8], maxlen=5) O(k)
# dq.extendleft([3, 2, 1])  # deque([1, 2, 3, 4, 5], maxlen=5) O(k)
# dq.remove(4)  # deque([1, 2, 3, 5], maxlen=5) O(n)
# # if the queue is full the insert will throw an error
# dq.insert(-1, 4)  # deque([1, 2, 3, 4, 5], maxlen=5) O(n)
# # index -1 is penultimate position, not last
# dq.reverse()  # deque([5, 4, 3, 2, 1], maxlen=5) O(n)
# dq.append(1)  # deque([4, 3, 2, 1, 1], maxlen=5) O(1)
# dq.count(1)  # returned 2 O(n)
# dq.rotate(1)  # deque([1, 4, 3, 2, 1], maxlen=5) O(k)
# dq.rotate(3)  # deque([3, 2, 1, 1, 4], maxlen=5) O(k)
# dq.rotate(1)  # deque([4, 3, 2, 1, 1], maxlen=5) O(k)
# f = dq.copy()  # deque([4, 3, 2, 1, 1], maxlen=5) O(n)
# dq.clear()  # deque([], maxlen=5)
# lst_in = list(map(int, input().split()))  # 1 2 3 5 4 11 7 23 24 25 19 23
# q = deque(lst_in)  # deque([1, 2, 3, 5, 4, 11, 7, 23, 24, 25, 19, 23])
# print(*[q.popleft() for i in range(3)])  # 1 2 3 # deque([5, 4, 11, 7, 23, 24, 25, 19, 23])

# lst_in = list(map(str.strip, input().split()))  # этот список в программе не менять
# q = deque(lst_in)
# q.insert(2, "run")
# q.remove("edit")
# print(q)

# data = list(map(int, input().split()))  # этот список в программе не менять
# buff = deque(list(reversed(data))[:10], maxlen=10)
# print(*[buff.pop() for i in range(3)])


# lst_in = list(map(str.strip, sys.stdin.readlines()))
# back_url = deque(lst_in, maxlen=20)
# print(back_url.pop())

# data = list(map(int, input().split()))
# lifo = data[:]
# print(*[lifo.pop() for i in range(2)])