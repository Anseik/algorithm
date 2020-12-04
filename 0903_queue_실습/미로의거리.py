import sys
sys.stdin = open('미로의거리.txt')

def bfs(r, c, length):

    # 델타(사방)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 방문표시
    visited = [[0] * N for _ in range(N)]

    # 큐 생성
    Q = []
    Q.append((r, c, length))
    while Q:
        cr, cc, length = Q.pop(0)
        visited[cr][cc] = 1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if maze[nr][nc] == 0:
                    Q.append((nr, nc, length + 1))
                elif maze[nr][nc] == 3:
                    return length

    return 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(N)
    # print(maze)

    # 시작점 찾기
    sr = 0
    sc = 0
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr = r
                sc = c
    # print(sr, sc)

    # bfs함수 실행
    result = bfs(sr, sc, 0)
    print("#{} {}".format(tc, result))


