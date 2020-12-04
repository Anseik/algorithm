# import sys
# sys.stdin = open('boj_1113_수영장만들기.txt')

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(r, c, h):
    global water
    check[r][c] = 1
    Q = list()
    Q.append((r, c))
    fill = 1
    can = True
    while Q:
        cr, cc = Q.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                can = False
                continue  # 갈 수 있는 모든 칸을 체크하기위해서 바로 return하지 않고 Q가 빌때까지 계속 탐색한다.

            if pool[nr][nc] <= h and not check[nr][nc]:
                check[nr][nc] = 1
                Q.append((nr, nc))
                fill += 1
    if can:
        water += fill



N, M = map(int, input().split())
pool = [list(map(int, input())) for _ in range(N)]
# print(N, M, pool)

# 가장자리에 있는 칸은 확인할 필요 없다.
# 0 < r < N - 1 and 0 < c < M - 1 범위만 확인하면 된다.

# 최대 채울 수 있는 물의 높이는 가장 높은 칸의 높이와 같다.
# 물을 채울 수 있는 곳은 bfs를 실행했을때 가장자리로 이동하지 않는 칸이다.

# 물을 채웠을때 흐른다 == 현재 높이가 같거나 낮다.

# 물을 더 이상 채울 수 없는곳 즉, 물을 채우면 흘러내리는 곳의 위치 정보를 저장해 놓는다.

# bfs한번에 물을 채울 수 있는 곳에 모두 물을 채우도록 설계한다.

# 물은 1씩 채워 나간다.

maxh = 0
for i in range(N):
    for j in range(M):
        if maxh < pool[i][j]:
            maxh = pool[i][j]

water = 0
# h는 물이 채워졌을때 높이
for h in range(1, maxh + 1):
    check = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if pool[r][c] <= h and not check[r][c]:
                bfs(r, c, h)

print(water)