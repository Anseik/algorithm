import sys
sys.stdin = open('swea_5250_최소비용.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    Q = list()
    Q.append((r, c))
    while Q:
        cr, cc = Q.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if H[nr][nc] > H[cr][cc]: # 다음 이동할 곳이 더 높은 곳이면
                    tmp = weight[cr][cc] + 1 + (H[nr][nc] - H[cr][cc])
                else:
                    tmp = weight[cr][cc] + 1
                if weight[nr][nc] > tmp:
                    weight[nr][nc] = tmp
                    Q.append((nr, nc))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    INF = 0xfffffffff
    weight = [[INF] * N for _ in range(N)]
    weight[0][0] = 0
    bfs(0, 0)

    result = weight[N - 1][N - 1]
    print('#{} {}'.format(tc, result))