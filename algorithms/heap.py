#siftdown is implemented only for solving tasks on the stepik

from math import ceil

heap = []


def siftup(index):
    if index != 0:
        if heap[index] > heap[ceil((index-1)/2)]:
            heap[index], heap[ceil((index-1)/2)] = heap[ceil((index-1)/2)], heap[index]
            siftup(ceil((index-1)/2))

def siftdown(index):
    if len(heap) >= index * 2 + 2:
        if heap[index * 2] > heap[index * 2 + 1]:
            heap[index], heap[index * 2] = heap[index * 2], heap[index]
            siftdown(index * 2)
        else:
            heap[index], heap[index * 2 + 1] = heap[index * 2 + 1], heap[index]
            siftdown(index * 2 + 1)
    elif len(heap) == index * 2 + 1:
        heap[index], heap[index * 2] = heap[index * 2], heap[index]
        heap.pop(-1)

for i in range(int(input())):
    command = input().split()
    if command[0] == "Insert":
        heap.append(int(command[1]))
        siftup(len(heap)-1)
    if command[0] == "ExtractMax":
        print(heap[0])
        heap[0] = -10000000
        siftdown(0)