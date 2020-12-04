import math
import sys
sys.stdin = open('SWEA_10570_제곱펠린드롬.txt')

def pal(num):
    target = str(num)
    N = len(target)
    M = N // 2
    for i in range(M):
        if target[i] == target[N - 1 - i]:
            continue
        return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    A1, B1 = math.ceil(A ** 0.5), math.floor(B ** 0.5)

    cnt = 0
    for num in range(A1, B1 + 1):
        if pal(num) and pal(num ** 2):
            cnt += 1

    print("#{} {}".format(tc, cnt))