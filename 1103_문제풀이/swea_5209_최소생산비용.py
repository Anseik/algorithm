import sys
sys.stdin = open('swea_5209_최소생산비용.txt')


def perm(idx, cost):
    # idx : 제품번호, cost 현재까지 생산비용
    global min_cost
    # 백트래킹 : 현재까지 생산비용이 정답후보보다 크면 더 이상 탐색할 필요 없다.
    if cost >= min_cost:
        return
    if idx == N:
        min_cost = min(min_cost, cost)
        return
    for i in range(N):
        if not fac[i]:
            fac[i] = 1
            perm(idx + 1, cost + arr[idx][i])
            fac[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    fac = [0] * N
    min_cost = 15 * 99
    perm(0, 0)
    print('#{} {}'.format(tc, min_cost))

