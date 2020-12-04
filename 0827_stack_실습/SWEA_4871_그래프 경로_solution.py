import sys
sys.stdin = open('SWEA_4871_그래프 경로_안세익.txt')

def DFS(v):
    visit[v] = 1
    if v == e:
        return 1
    for w in range(1, V+1):
        if G[v][w] == 1 and visit[w] == 0:
            if DFS(w) == 1:
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    # V : 정점, E: 간선
    V, E = map(int, input().split())
    # 인접 행렬, 정점 번호 1 ~ V
    G = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E): # 간선 정보 읽기
        u, v = map(int, input().split())
        G[u][v] = 1

    s, e = map(int, input().split())

    visit = [0] * (V+1)

    print(DFS(s))