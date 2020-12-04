import sys
from heapq import heapify
sys.stdin = open('이진힙.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    heapify(arr)
    print(arr)

    # 루트가 0이다.
    # 왼쪽 자식 : 2 * i + 1
    # 오른쪽 자식 : 2 * i + 2
    # 부모 : (i - 1) // 2
    # 맨마지막 노드의 인덱스 : N - 1