import sys
sys.stdin = open('swea_1865_동철이의일분배.txt')

def distribution(p, curper):
    global max_per
    if curper < max_per:
        return

    if p == N:
        max_per = max(max_per, curper)
        return

    for j in range(N):
        if not jobs[j] and per[p][j]:
            jobs[j] = 1
            distribution(p + 1, curper * per[p][j])
            jobs[j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    per = [list(map(lambda x: x / 100, list(map(int, input().split())))) for _ in range(N)]
    # print(N)
    # print(per)

    jobs = [0] * N
    max_per = 0
    distribution(0, 1)
    result = format(max_per * 100, '.6f')
    print('#{} {}'.format(tc, result))