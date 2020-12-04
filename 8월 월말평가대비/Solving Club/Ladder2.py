import sys
sys.stdin = open('Ladder2.txt')


def dfs(r, c):
    visited[r][c] = 1
    global cnt
    cnt += 1
    for d in range(3):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and ladder[nr][nc] == 1 and visited[nr][nc] == 0:
            return dfs(nr, nc)

    else:
        return cnt

T = 10
N = 100
for _ in range(T):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(N)]
    # print(ladder)

    # 델타
    dr = [0, 0, 1]
    dc = [-1, 1, 0]

    result = 0
    min_distance = N * N

    # 시작점 찾고 dfs실행
    for i in range(N):
        if ladder[0][i] == 1:
            r, c = 0, i
            cnt = 0
            visited = [[0] * N for _ in range(N)]
            # print(dfs(r, c))
            distance = dfs(r, c)
            if distance < min_distance:
                min_distance = distance
                result = i

    print("#{} {}".format(tc, result))