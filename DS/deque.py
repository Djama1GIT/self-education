# from collections import deque

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
lst_in = list(map(int, input().split()))  # 1 2 3 5 4 11 7 23 24 25 19 23
q = __import__("collections").deque(lst_in)  # deque([1, 2, 3, 5, 4, 11, 7, 23, 24, 25, 19, 23])
print(*[q.popleft() for i in range(3)])  # 1 2 3 # deque([5, 4, 11, 7, 23, 24, 25, 19, 23])
