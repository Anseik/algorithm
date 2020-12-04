import math
import sys
sys.stdin = open('BOJ_13300_방배정.txt')

T = 1
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    info = [[0] * 2 for _ in range(7)]
    # print(info)

    for i in range(N):
        S, Y = map(int, input().split())
        info[Y][S] += 1
    # print(info)

    cnt = 0
    for m in range(1, 7):
        for n in range(0, 2):
            cnt += math.ceil(info[m][n] / K)

    print(cnt)

