import sys
sys.stdin = open('노드의거리.txt')

def bfs(v, l):
    global G

    # 방문체크
    visited = [0] * (V+1)

    # 큐생성
    Q = []
    Q.append((v, l))

    # bfs실행
    while Q:
        cv, cl = Q.pop(0) #현재노드, 현재 지난 간선 개수
        visited[cv] = 1
        for w in range(1, V+1):
            if adj[cv][w] == 1 and visited[w] == 0:
                if w == G:
                    return cl + 1
                Q.append((w, cl + 1))
    return 0

T = int(input())
for tc in range(1, T+1):
    # 노드V, 간선E
    V, E = map(int, input().split())
    # print(V, E)

    # 인접행렬
    adj = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        adj[s][e] = 1
        adj[e][s] = 1
    # print(adj)

    # 출발노드S, 도착노드G
    S, G = map(int, input().split())
    # print(S, G)



    result = bfs(S, 0)
    print("#{} {}".format(tc, result))



