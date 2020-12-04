import sys
sys.stdin = open('노드의거리.txt')

def bfs(v, distance):
    Q = []
    Q.append((v, distance))
    visit = [0] * (V + 1)
    while Q:
        v, distance = Q.pop(0)
        if v == G:
            return distance
        visit[v] = 1
        for w in range(1, V + 1):
            if w in adj[v] and not visit[w]:
                Q.append((w, distance + 1))

    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for i in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    S, G = map(int, input().split())
    # print(V, E)
    # print(adj)
    # print(S, G)

    result = bfs(S, 0)
    print("#{} {}".format(tc, result))