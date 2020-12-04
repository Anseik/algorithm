import sys
sys.stdin = open('창용 마을 무리의 개수.txt')

def dfs(v):
    visit[v] = 1
    for w in range(1, N + 1):
        if adj[v][w] and not visit[w]:
            dfs(w)

T = int(input())
for tc in range(1, T+1):
    # N : 사람수, M : 관계수
    N, M = map(int, input().split())

    # 인접행렬
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        p1, p2 = map(int, input().split())
        adj[p1][p2] = 1
        adj[p2][p1] = 1
    # print(N, M)
    # print(adj)

    # 방문체크
    visit = [0] * (N + 1)

    group = 0
    for i in range(1, N + 1):
        if visit[i] == 0:
            group += 1
            dfs(i)

    print("#{} {}".format(tc, group))

