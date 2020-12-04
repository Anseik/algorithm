import sys
sys.stdin = open('boj_1012_유기농배추_안세익.txt')

def dfs(r, c):
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr, nc)

T = int(input())
for tc in range(1, T+1):
    # M : 가로길이(열 길이), N : 세로길이(행 길이), K : 배추 개수
    M, N, K = map(int, input().split())
    # print(M, N, K)

    field = [[0] * M for _ in range(N)] # 밭을 만든다.

    for i in range(K): # 배추를 심는다.
        x, y = map(int, input().split()) # x는 가로(열), y는 세로(행)
        field[y][x] = 1
    # print(field)

    # 델타를 이용하여 사방을 탐색하면서 이동한다.
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 방문 표시
    visited = [[0] * M for _ in range(N)]

    # 모든 밭을 순회하면서 1을 만나면 dfs를 실행 dfs를 최초 실행하게 되는 횟수를 카운트
    # dfs로 순회한 배추의 위치는 0으로 바꾼다.
    cnt = 0
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1 and visited[r][c] == 0:
                cnt += 1
                dfs(r, c)

    print(cnt)