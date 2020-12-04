import sys
sys.stdin = open('Ladder1.txt')

def dfs(r, c):
    # dfs실행
    stack = list()
    stack.append((r, c))
    while stack:
        cr, cc = stack.pop()
        visited[cr][cc] = 1
        for d in range(3):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if ladder[nr][nc] == 1:
                    stack.append((nr, nc))
                    break
                elif ladder[nr][nc] == 2:
                    return c
    return -1

T = 10
N = 100
for _ in range(10):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(N)]
    # print(tc)
    # print(ladder)

    # 델타(좌, 우, 하)
    dr = [0, 0, 1]
    dc = [-1, 1, 0]
    # 시작점 찾기
    for i in range(N):
        if ladder[0][i] == 1:
            r, c = 0, i
            visited = [[0] * N for _ in range(N)]
            result = dfs(r, c)
            if result != -1:
                 break



    print("#{} {}".format(tc, result))



