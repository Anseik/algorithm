import sys
sys.stdin = open('노드의거리.txt')

T = int(input())
for tc in range(1, T+1):
    # 노드V, 간선E
    V, E = map(int, input().split())
    # print(V, E)

    # 인접행렬
    G = [[0] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    # 출발노드s, 도착노드e
    s, e = map(int, input().split())

    # 방문표시
    visit = [0] * (V + 1)
    Q = [s]
    visit[s] = 1 # 출발점 방문하고 큐에 삽입

    while Q: # 빈큐가 아닐 동안
        v = Q.pop(0) # 큐에서 뺀다.
        # v의 인접 정점 중 방문하지 않은 정점을 찾는다.
        for w in G[v]:
            if not visit[w]:
                visit[w] = visit[v] + 1 # 거리 계산
                if w == e:
                    Q.clear()
                    break
                Q.append(w)


    print(visit[e] - 1)