import sys

sys.stdin = open('boj_1113_수영장만들기.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    visit[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        # 물을 채우면 다음 칸으로 흘러 갈 수 있을때(다음 칸이 현재 칸보다 높이가 낮거나 같을때)
        if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
            if pool[nr][nc] <= pool[r][c]:
                if dfs(nr, nc):
                    return 1
        # 물이 땅으로 흘러 갈때(경계를 벗어 낫을때)
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            return 1


N, M = map(int, input().split())
pool = [list(map(int, input())) for _ in range(N)]
# print(N, M)
# print(pool)

water = 0
while True:
    cnt = 0
    for r in range(N):
        for c in range(M):
            visit = [[0] * M for _ in range(N)]
            if not dfs(r, c): # 물을 채울 수 있을 때
                pool[r][c] += 1
                water += 1
                cnt += 1
    if cnt == 0:
        break

print(water)


