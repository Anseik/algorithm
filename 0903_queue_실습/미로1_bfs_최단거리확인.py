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

    queue = list()
    queue.append((r, c, 0)) # 세번째 인자는 시작점으로부터 거리

    while queue:
        cr, cc, length = queue.pop(0)
        visited[cr][cc] = 1

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < L and 0 <= nc < L and not visited[nr][nc]:
                if maze[nr][nc] == 0:
                    queue.append((nr, nc, length + 1)) # nr,nc는 현재경로보다 거리가 1멀다.
                elif maze[nr][nc] == 3:

                    return length + 1 # bfs에서는 가장 먼저 찾은 경로가 최단거리 경로이다!!
                    # dfs에서는 가장 먼저 찾은 경로가 최단거리 경로가 아니다!!, 모든 경로를 찾고 길이비교를 따로 해야한다.

    return 0


T = 10
L = 16
for _ in range(T):
    tc = input()
    maze = [list(map(int, input())) for _ in range(L)]
    # print(maze)
    visited = [[0] * L for _ in range(L)]
    result = bfs()
    # print(visited)
    print("#{} {}".format(tc, result))
