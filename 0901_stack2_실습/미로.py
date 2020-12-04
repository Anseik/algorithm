import sys
sys.stdin = open('미로.txt')


# def route(r, c):
#     # 델타 상하좌우
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     stack = []
#     stack.append((r, c))
#     visited[r][c] = 1
#     while stack:
#         cr, cc = stack.pop()
#         if maze[cr][cc] == "3":
#             return 1
#         for d in range(4):
#             nr = cr + dr[d]
#             nc = cc + dc[d]
#             if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and maze[nr][nc] != "1":
#                 stack.append((nr, nc))
#                 visited[nr][nc] = 1
#
#     return 0


def route2(r, c):
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
            if route2(nr, nc) == 1:
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    # print(N)

    sr = 0
    sc = 0
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                sr = r
                sc = c
                break
    # print(sr, sc)

    # 방문체크
    visited = [[0] * N for _ in range(N)]

    # 스택을 이용한 dfs
    # result = route(sr, sc)
    # print("#{} {}".format(tc, result))

    # 재귀를 이용한 dfs
    answer = route2(sr, sc)
    print("#{} {}".format(tc, answer))