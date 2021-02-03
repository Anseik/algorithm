import sys
import heapq
sys.stdin = open('swea-1249-보급로.txt')

def dijkstra():
    # 해당 위치까지 가는데 드는 최소 복구 시간을 저장할 배열 생성, 시작점 초기화
    INF = 987654321
    cost = [[INF] * N for _ in range(N)]
    cost[0][0] = 0

    # 힙 생성
    heap = []
    heapq.heappush(heap, (0, 0, 0)) # 복구시간, 행, 렬
    while heap:
        ct, cr, cc = heapq.heappop(heap)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                nt = ct + arr[nr][nc]
                if cost[nr][nc] > nt:
                    cost[nr][nc] = nt
                    heapq.heappush(heap, (nt, nr, nc))

    return cost[N - 1][N - 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 다익스트라 실행
    result = dijkstra()

    print('#{} {}'.format(tc, result))