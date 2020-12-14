import sys
sys.stdin = open('boj_15954_인형들.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

min_s = float('inf')
for i in range(K, N + 1):
    for j in range(N - i + 1):
        tmp = arr[j : j + i]
        # 평균
        m = sum(tmp) / i
        # 분산
        v = 0
        for a in tmp:
            v += (a - m) ** 2
        v /= i
        # 표준편차
        s = v ** (0.5)
        # 표준편차의 최소값
        min_s = min(min_s, s)

print(min_s)



