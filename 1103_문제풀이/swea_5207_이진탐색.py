import sys
sys.stdin = open('swea_5207_이진탐색.txt')

def binary_search(before, l, r, key):
    # before : 0 초기값 / -1 왼쪽 / 1 오른쪽
    global status
    if l > r:
        return -1
    mid = (l + r) // 2
    if A[mid] == key:
        return mid
    elif A[mid] > key: # 왼쪽 탐색
        if before == -1: # 이전에도 왼쪽을 탐색했으면 조건을 만족하지 않는다.
            status = False
        return binary_search(-1, l, mid - 1, key)
    elif A[mid] < key: # 오른쪽 탐색
        if before == 1: # 이전에도 오른쪽을 탐색했으면 조건을 만족하지 않는다.
            status = False
        return binary_search(1, mid + 1, r, key)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    cnt = 0
    for key in B:
        status = True
        if binary_search(0, 0, N - 1, key) != -1:
            if status:
                cnt += 1

    print("#{} {}".format(tc, cnt))