import sys
sys.stdin = open('swea_5189_전자카트_solution.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]
    # print(N, arr)

    order = [i for i in range(N)]

    ans = 0xffffffffff
    def perm(k, cost):
        global ans
        if cost >= ans:
            return
        if k == N:
            cost += G[order[N - 1]][0]
            ans = min(ans, cost)
        else:
            for i in range(k, N):
                order[k], order[i] = order[i], order[k]
                perm(k + 1, cost + G[order[k-1]][order[k]])
                order[k], order[i] = order[i], order[k]

    perm(1, 0)
    print('#{} {}'.format(tc, ans))
