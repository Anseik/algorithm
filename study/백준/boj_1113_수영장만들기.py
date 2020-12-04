import sys
sys.stdin = open('boj_1113_수영장만들기.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check_status(r, c):
    for d in range(4):  # 물을 채울 수 있는 곳과 없는 곳을 구분
        nr = r + dr[d]
        nc = c + dc[d]
        # 경계와 접해 있으면 물을 더이상 채울 수 없다.
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            status[r][c] = 0
            return 0
        # 현재 칸의 높이보다 낮은 칸이 사방에 있으면 더 이상 물을 채울 수 없다.
        elif pool[nr][nc] < pool[r][c]:
            status[r][c] = 0
            return 0
    else:
        return 1

def dfs(r, c):
    visit[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        # 물이 땅으로 흘러 갈때
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            return 0
        # 현재 칸의 높이보다 낮은 칸이 사방에 있으면 더 이상 물을 채울 수 없다.
        elif pool[nr][nc] < pool[r][c]:
            dfs(r, c)
    # 물이 빠져나갈 수 없을때
    return 1

N, M = map(int, input().split())
pool = [list(map(int, input())) for _ in range(N)]
# print(N, M)
# print(pool)

before = 0 # 최초 시작 높이의 합
for r in range(N):
    for c in range(M):
        before += pool[r][c]
# print(before)

while True:
    status = [[1] * M for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(M):
            if check_status(r, c):
                pool[r][c] += 1
                cnt += 1
    # print(pool)
    if cnt == 0: # 더 이상 물을 채울 수 있는 곳이 없으면
        break

    # dfs(조건 : 현재 높이보다 같거나 낮은 곳이 있을경우)를 통해 경계밖으로 벗어날 수 있으면 채운물은 다시 빠진다.

    flow = 0
    visit = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            dfs(r, c)
