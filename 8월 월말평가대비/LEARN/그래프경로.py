import sys
sys.stdin = open('그래프경로.txt')

def dfs(v):
    visited[v] = 1
    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)

    return visited[G]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # print(V, E)

    # 인접행렬
    adj = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        adj[s][e] = 1

    # print(adj)
    S, G = map(int, input().split())
    # print(S, G)

    visited = [0] * (V+1)

    result = dfs(S)
    print("#{} {}".format(tc, result))


