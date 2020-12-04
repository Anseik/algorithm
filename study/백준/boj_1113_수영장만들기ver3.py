# import sys
# sys.stdin = open('boj_1113_수영장만들기.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# def dfs(r, c):
#     stack = list()
#     stack.append((r, c))
#     while stack:
#         cr, cc = stack[-1]
#         if flow[cr][cc] == 1: # 이동한 곳이 물이 흐르는 칸이면
#             flow[r][c] = 1
#             return 0
#         visit[cr][cc] = 1
#         for d in range(4):
#             nr = cr + dr[d]
#             nc = cc + dc[d]
#             if 0 <= nr < N and 0 <= nc < M:
#                 # 경계를 벗어나지 않고 흐를 수 있으면
#                 if visit[nr][nc] == 0 and pool[nr][nc] <= pool[r][c]:
#                     stack.append((nr, nc))
#                     break
#             else: # 경계를 벗어나면
#                 flow[r][c] = 1 # 최초 시작한 위치는 더 이상 물을 채울 수 없는 곳
#                 return 0 # 물을 채울 수 없다.
#         else:
#             stack.pop()
#     return 1 # 물을 채울 수 있다.


def bfs(r, c):
    Q = list()
    Q.append((r, c))
    fill = 1
    while Q:
        cr, cc = Q.pop(0)
        if flow[cr][cc] == 1:
            flow[r][c] = 1
            return 0
        visit[cr][cc] = 1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                # 경계를 벗어나지 않고 흐를 수 있으면
                if visit[nr][nc] == 0 and pool[nr][nc] <= pool[r][c]:
                    Q.append((nr, nc))
                    fill += 1
            else:  # 경계를 벗어나면
                flow[r][c] = 1  # 최초 시작한 위치는 더 이상 물을 채울 수 없는 곳
                return 0  # 물을 채울 수 없다.

    return fill  # 물을 채울 수 있다.



N, M = map(int, input().split())
pool = [list(map(int, input())) for _ in range(N)]
max_fill = 0
for i in range(N):
    for j in range(M):
        if max_fill < pool[i][j]:
            max_fill = pool[i][j]

# 채운 물의 양
water = 0
# 물이 흐르는 곳, 더 이상 물을 채울 수 없는곳(앞으로도 확인할 필요 없음) 위치정보 저장(memoization)
flow = [[0] * M for _ in range(N)]
for h in range(1, m_fill + 1):
    fill_cnt = 0
    visit = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if not flow[r][c] and pool[r][c] < h and not visit[r][c]: # 이미 물을 더 이상 채울 수 없는 곳으로 판정된 곳이 아니면
                cnt = bfs(r, c)
                if cnt:
                    visit = [[0] * M for _ in range(N)]
                    # pool[r][c] += 1
                    fill_cnt += cnt
    water += fill_cnt
print(water)


