from bisect import bisect_left, bisect_right
segments_left, segments_right = [], []
count_n, _ = map(int, input().split())
for i in range(count_n):
    left_point, right_point = map(int, input().split())
    segments_left += [left_point]
    segments_right += [right_point]
points = list(map(int, input().split()))
segments_left.sort()
segments_right.sort()
for i in points:
    print(bisect_right(segments_left, i) - bisect_left(segments_right, i), end=" ")