import sys
sys.stdin = open('swea_5209_최소생산비용_solution.txt')

def solve(idx, cost):
    global min_cost
    if cost >= min_cost:
        return
    if idx == N:
        min_cost = cost
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            solve(idx + 1, cost + costs[idx][i])
            used[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(costs)
    used = [0] * N
    min_cost = 0xffffffff
    solve(0, 0)
    print('#{} {}'.format(tc, min_cost))

