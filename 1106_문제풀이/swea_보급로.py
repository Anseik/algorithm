import sys
import heapq
sys.stdin = open('swea_보급로.txt')

def dijkstra():
    INF = 987654321
    time = [[INF] * N for _ in range(N)]
    time[0][0] = 0

    heap = []
    # 복구시간 / 행 / 렬
    heapq.heappush(heap, (0, 0, 0))

    while heap:
        ct, cr, cc = heapq.heappop(heap)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                nt = ct + arr[nr][nc]
                if time[nr][nc] > nt:
                    time[nr][nc] = nt
                    heapq.heappush(heap, (nt, nr, nc))

    return time[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    result = dijkstra()
    print('#{} {}'.format(tc, result))