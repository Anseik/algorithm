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
    nums = list(map(int, input().split()))

    heap = [0] * (N + 1)
    heapcount = 0
    for i in nums:
        heappush(i)

    # print(heap)
    total = 0
    cur = heapcount
    parent = cur // 2
    while parent:
        total += heap[parent]
        cur = parent
        parent = cur // 2

    print("#{} {}".format(tc, total))