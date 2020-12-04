import sys
sys.stdin = open('swea_5251_최소이동거리_solution.txt')

def dijkstra():
    dist = [987654321] * (V + 1)

    visited = [False] * (V + 1)
    dist[0] = 0

    for _ in range(V + 1):
        min_idx = -1
        min_value = 987654321

        for i in range(V + 1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = True

        for j in range(V + 1):
            if not visited[j] and dist[j] > dist[min_idx] + adj[min_idx][j]:
                dist[j] = dist[min_idx] + adj[min_idx][j]

    return dist[V]


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj = [[987654321] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        st, ed, w = map(int, input().split())

        adj[st][ed] = w

    ans = dijkstra()
    print('#{} {}'.format(tc, ans))