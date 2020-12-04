import sys
sys.stdin = open('회전.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # M은 최대 1000
    # 선형큐
    # Q = list(map(int, input().split())) + ([0] * M)
    # 원형큐
    Q = [0] + list(map(int, input().split()))
    # 선형큐
    # f, r = -1, N - 1
    # 원형큐
    f, r = 0, N
    SIZE = N + 1

    # 선형큐 사용
    # for _ in range(M):
    #     f += 1 # Q[f]
    #     r += 1
    #     Q[r] = Q[f]
    #
    # print(Q[f + 1])

    # 원형큐
    for _ in range(M):
        f = (f + 1) % SIZE
        r = (r + 1) % SIZE
        Q[r] = Q[f]

    print(Q[(f + 1) % SIZE])


    # 모듈러 연산
    # print(Q[M % N])

