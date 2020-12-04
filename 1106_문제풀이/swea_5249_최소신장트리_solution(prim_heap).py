import sys
import heapq

sys.stdin = open('swea_5249_최소신장트리_solution.txt')


def MST_PRIM():
    visited = [False] * (V + 1) # 정점의 선택여부
    heap = []
    # 가중치, 정점순으로 넣어야 가중치가 최소인 것을 찾을 수 있다.
    heapq.heappush(heap, (0, 0))
    ans = 0

    while heap:
        w, v = heapq.heappop(heap)  # 가중치, 정점
        if not visited[v]:
            ans += w
            visited[v] = True

            for node, weight in adj[v]:
                if not visited[node]:
                    heapq.heappush(heap, (weight, node))

    return ans


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접리스트
    adj = [[] for _ in range(V + 1)]

    for i in range(E):
        A, B, W = map(int, input().split())

        adj[A].append((B, W))
        adj[B].append((A, W))

    ans = MST_PRIM()
    print('#{} {}'.format(tc, ans))
