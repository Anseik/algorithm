import sys
sys.stdin = open('미로1.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    # 시작점 찾고
    r = 0
    c = 0
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                r, c = i, j
                break

    visited = [[0] * L for _ in range(L)]
    queue = list()
    queue.append((r, c))
    while queue:
        cr, cc = queue.pop(0)
        visited[cr][cc] = 1

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < L and 0 <= nc < L and not visited[nr][nc]:
                if maze[nr][nc] == 0:
                    queue.append((nr, nc))
                elif maze[nr][nc] == 3:
                    return 1

    return 0


T = 10
L = 16
for _ in range(T):
    tc = input()
    maze = [list(map(int, input())) for _ in range(L)]
    # print(maze)

    result = bfs()
    print("#{} {}".format(tc, result))
