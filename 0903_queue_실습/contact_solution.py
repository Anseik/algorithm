import sys
sys.stdin = open('contact.txt')

T = 10
V = 100
for tc in range(1, T+1):
    N, s = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접 행렬
    G = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(0, N, 2): # arr[i] --> arr[i + 1]
        G[arr[i]][arr[i+1]] = 1

    # 방문표시 및 거리
    visit = [0] * (V + 1)
    Q = [s]
    visit[s] = 1

    while Q:
        v = Q.pop(0)
        for w in range(1, V+1):
            if G[v][w] and not visit[w]:
                visit[w] = visit[v] + 1
                Q.append(w)

    ans = 1
    for i in range(2, V+1):
        if visit[ans] <= visit[i]:
            ans = i

    print(ans)