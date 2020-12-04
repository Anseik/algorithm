import sys
sys.stdin = open('이진힙.txt')

def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur // 2
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tmp = list(map(int, input().split()))
    # print(N)
    # print(tmp)

    heap = [0] * (N + 1)
    heapcount = 0
    for value in tmp:
        heappush(value)
    # print(heap)

    cur = heapcount
    parent = cur // 2
    result = 0
    while parent:
        result += heap[parent]
        cur = parent
        parent = cur // 2

    print("#{} {}".format(tc, result))
