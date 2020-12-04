import sys
sys.stdin = open('Ladder1.txt')

T = 10
N = 100
for _ in range(10):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(N)]
    # print(tc)
    # print(ladder)

    end = 0
    for i in range(N):
        if ladder[99][i] == 2:
            end = i

    # print(end)
    visited = [[0] * N for _ in range(N)]


    # 델타(좌, 우, 상)
    dr = [0, 0, -1]
    dc = [-1, 1, 0]
    r = 99
    c = end

    while r != 0:
        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and ladder[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                r, c = nr, nc
                break

    print("#{} {}".format(tc, c))



