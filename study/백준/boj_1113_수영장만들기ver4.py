# import sys
# sys.stdin = open('boj_1113_수영장만들기.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, h):
    global water
    stack = list()
    stack.append((r, c))
    visited[r][c] = 1
    fill = 1
    while stack:
        cr, cc = stack[-1]
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            # 경계를 벗어나면 물을 채울 수 없다.
            if not (0 <= nr < N and 0 <= nc < M):
                return

            if pool[nr][nc] < h and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                fill += 1
                break

        else:
            stack.pop()
    water += fill


N, M = map(int, input().split())
pool = [list(map(int, input())) for _ in range(N)]

# 채울 수 있는 최대 높이
maxh = 0
for i in range(N):
    if maxh < max(pool[i]):
        maxh = max(pool[i])

water = 0
for h in range(1, maxh + 1): # 1부터 채울 수 있는 최대 높이까지
    visited = list([0] * M for _ in range(N))
    for r in range(N):
        for c in range(M):
            if pool[r][c] < h and not visited[r][c]: # 높이가 h보다 낮거나 같고, 방문하지 않았으면
                dfs(r, c, h)

print(water)