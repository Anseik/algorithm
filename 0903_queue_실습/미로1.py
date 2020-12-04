import sys
sys.stdin = open('미로1.txt')


def route(r, c):
    visited[r][c] = 1
    if maze[r][c] == "3":
        return 1

    # 델타 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and maze[nr][nc] != "1":
            if route(nr, nc) == 1:
                return 1
    return 0

T = 10
N = 16
for _ in range(T):
    tc = input()
    maze = [input() for _ in range(N)]
    # print(maze)

    sr = 1
    sc = 1
    # for r in range(N):
    #     for c in range(N):
    #         if maze[r][c] == '2':
    #             sr = r
    #             sc = c
    #             break
    # print(sr, sc)

    # 방문체크
    visited = [[0] * N for _ in range(N)]

    # 재귀를 이용한 dfs
    answer = route(sr, sc)
    print("#{} {}".format(tc, answer))