import sys
import heapq
sys.stdin = open('swea_5251_최소이동거리_solution.txt')

def dijkstra_heap():
    dist = [987654321] * (V + 1)
    visited = [False] * (V + 1)

    heap = []
    dist[0] = 0
    heapq.heappush(heap, (0, 0))

    while heap:
        w, v = heapq.heappop(heap)

        if not visited[v]:
            visited[v] = True
            dist[v] = w

            for i in range(V + 1):
                if not visited[i] and dist[i] > dist[v] + adj[v][i]:
                    heapq.heappush(heap, (dist[v] + adj[v][i], i))

    return dist[V]


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj = [[987654321] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        st, ed, w = map(int, input().split())

        adj[st][ed] = w

    ans = dijkstra_heap()
    print('#{} {}'.format(tc, ans))