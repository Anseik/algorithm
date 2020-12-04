import sys
sys.stdin = open('SWEA_4871_그래프 경로_안세익.txt')

def dfs(v):
    visited[v] = 1
    # 간선으로 연결된 노드 중에서 방문하지 않은 노드에서 dfs 재귀 호출
    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)
    return visited[G]

T = int(input())
for tc in range(1, T+1):
    # V : 노드의 개수, E: 간선의 개수
    V, E = map(int, input().split())
    # print(V, E)

    # 인접행렬
    adj = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        adj[s][e] = 1

    # print(adj)

    # S : 출발노드, G: 도착노드
    S, G = map(int, input().split())
    # print(S, G)

    # 방문 체크
    visited = [0] * (V+1)

    # dfs 실행
    result = dfs(S)

    print("#{} {}".format(tc, result))


