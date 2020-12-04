import sys
sys.stdin = open('미로1.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 반복문을 이용한 dfs
def dfs():
    # 시작점 찾고
    r = 0
    c = 0
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                r, c = i, j
                break

    stack = list()
    stack.append((r, c))
    visited = [[0] * L for _ in range(L)] # 지나온 경로 표시

    # 시작점 찾으면 dfs 실행
    # 앞단 부터 순회(pop을 나중에)
    while stack: # 스택이 비어있지 않으면 dfs계속 실행
        # dfs 실행 중 목적지 도달하면, return 1, 도달 하지 못하면 return 0
        cr,cc = stack[-1] # 현재 노드
        # 현재 노드에서 갈 수 있는 경로 탐색
        # 상하좌우 네방향, 미로 범위안, 벽이 아닌곳, 방문하지 않은 곳
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < L and 0 <= nc < L and visited[nr][nc] == 0:
                if maze[nr][nc] == 0:
                    stack.append((nr, nc))
                    visited[nr][nc] = 1
                    break
                elif maze[nr][nc] == 3:
                    return 1
        else:
            stack.pop()

    return 0

    # # 뒷단 부터 순회하는 방법(pop을 먼저)
    # while stack: # 스택이 비어있지 않으면 dfs계속 실행
    #     # dfs 실행 중 목적지 도달하면, return 1, 도달 하지 못하면 return 0
    #     cr,cc = stack.pop() # 현재 노드
    #     # 현재 노드에서 갈 수 있는 경로 탐색
    #     # 상하좌우 네방향, 미로 범위안, 벽이 아닌곳, 방문하지 않은 곳
    #     for d in range(4):
    #         nr = cr + dr[d]
    #         nc = cc + dc[d]
    #         if 0 <= nr < L and 0 <= nc < L and visited[nr][nc] == 0:
    #             if maze[nr][nc] == 0:
    #                 stack.append((nr, nc))
    #                 visited[nr][nc] = 1
    #             elif maze[nr][nc] == 3:
    #                 return 1
    #
    # return 0


def dfs2(r, c):
    visited2[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < L and 0 <= nc < L and not visited2[nr][nc]:
            if maze[nr][nc] == 0:
                if dfs2(nr, nc) == 1:
                    return 1
            elif maze[nr][nc] == 3: # 목적지 찾음
                return 1

    return 0


def bfs():
    # 시작점 찾고
    r = 0
    c = 0
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                r, c = i, j
                break

    visited3 = [[0] * L for _ in range(L)]
    queue = list()
    queue.append((r, c))
    while queue:
        cr, cc = queue.pop(0)
        visited3[cr][cc] = 1

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < L and 0 <= nc < L and not visited3[nr][nc]:
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
    visited2 = [[0] * L for _ in range(L)]  # 지나온 경로 표시
    result = bfs()
    print("#{} {}".format(tc, result))
