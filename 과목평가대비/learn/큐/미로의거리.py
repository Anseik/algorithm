import sys
sys.stdin = open('미로의거리.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, cnt):
    Q = []
    Q.append((r, c, cnt))
    while Q:
        cr, cc, cnt = Q.pop(0)
        visit[cr][cc] = 1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and maze[nr][nc] != 1:
                if maze[nr][nc] == 3:
                    return cnt
                else:
                    Q.append((nr, nc, cnt + 1))
    return 0




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(N)
    # print(maze)

    sr, sc = 0, 0
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c
    # print(sr, sc)

    visit = [[0] * N for _ in range(N)]
    result = bfs(sr, sc, 0)
    print("#{} {}".format(tc, result))
