import sys
from collections import deque
sys.stdin = open('swea_5204_병합정렬.txt')


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    left = deque(left)
    right = deque(right)
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())

        else:
            break

    if len(left) > 0:
        result += left
    elif len(right) > 0:
        result += right

    return result


def merge_sort(arr):
    # 기저영역
    n = len(arr)
    if n == 1:
        return arr
    left = arr[0:n//2]
    right = arr[n//2:n]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(N)
    # print(arr)
    cnt = 0
    L = merge_sort(arr)

    # print(sort_arr)
    print('#{} {} {}'.format(tc, L[N//2], cnt))

