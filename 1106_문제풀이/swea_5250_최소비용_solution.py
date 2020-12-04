import sys
import heapq
sys.stdin = open('swea_5250_최소비용_solution.txt')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():
    heap = []
    dist[0][0] = 0

    # 가중치, 행, 렬
    heapq.heappush(heap, (dist[0][0], 0, 0))

    while heap:
        curr_w, curr_r, curr_c = heapq.heappop(heap)
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                add_cost = arr[nr][nc] - arr[curr_r][curr_c]
                if add_cost < 0:
                    add_cost = 0
                new_w = curr_w + 1 + add_cost

                if dist[nr][nc] > new_w:
                    dist[nr][nc] = new_w
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))

    return dist[N - 1][N - 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dist = [[987654321] * N for _ in range(N)]

    ans = dijkstra()
    print('#{} {}'.format(tc, ans))

