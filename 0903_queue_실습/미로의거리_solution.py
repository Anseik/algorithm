import sys
sys.stdin = open('미로의거리.txt')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0] # 우 좌 하 상
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    # maze = [list(map(int, input())) for _ in range(N)]

    sx = sy = ex = ey = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == "2":
                sx, sy = i, j
            elif maze[i][j] == "3":
                ex, ey = i, j

    visit = [[0] * (N) for _ in range(N)]
    Q = [[sx, sy]]
    visit[sx][sy] = 1

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            # 경계체크, 통로인지, 방문정보
            if tx < 0 or tx == N or ty < 0 or ty == N: continue
            if maze[tx][ty] == "1" or visit[tx][ty]: continue
            visit[tx][ty] = visit[x][y] + 1
            if tx == ex and ty == ey:
                Q.clear(); break
            Q.append([tx, ty])

    if visit[ex][ey]: visit[ex][ey] -= 2
    print(visit[ex][ey])



