import sys
sys.stdin = open('미로1.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    visited[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < L and 0 <= nc < L and not visited[nr][nc]:
            if maze[nr][nc] == 0:
                if dfs(nr, nc) == 1:
                    return 1
            elif maze[nr][nc] == 3: # 목적지 찾음
                return 1

    return 0


T = 10
L = 16
for _ in range(T):
    tc = input()
    maze = [list(map(int, input())) for _ in range(L)]
    # print(maze)
    visited = [[0] * L for _ in range(L)]  # 지나온 경로 표시

    # 시작점 찾기
    r = 0
    c = 0
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                r, c = i, j
                break
    result = dfs(r, c)
    print("#{} {}".format(tc, result))
