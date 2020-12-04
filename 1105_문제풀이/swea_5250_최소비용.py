import sys
import heapq
sys.stdin = open('swea_5250_최소비용.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():
    U = set()
    while len(U) < N*N:
        # 가장 가중치가 작은것 선택
        min_w, r, c = heapq.heappop(heap)
        U.add((r, c))
        # 가중치를 갱신
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in U:
                if arr[nr][nc] > arr[r][c]: # 다음 이동할 곳이 더 높은 곳이면
                    tmp = min_w + 1 + (arr[nr][nc] - arr[r][c])
                else:
                    tmp = min_w + 1
                if weight[nr][nc] > tmp:
                    weight[nr][nc] = tmp
                    heapq.heappush(heap, [weight[nr][nc], nr, nc])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    INF = 0xfffffffff
    weight = [[INF] * N for _ in range(N)]
    weight[0][0] = 0

    heap = list()
    heapq.heappush(heap, [0, 0, 0])

    dijkstra()
    result = weight[N - 1][N - 1]
    print('#{} {}'.format(tc, result))