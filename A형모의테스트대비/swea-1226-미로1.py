import sys
sys.stdin = open('swea-1226-미로1.txt')

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, dist):
    Q = list()
    Q.append((r, c, dist))
    visit[r][c] = 1
    while Q:
        cr, cc, dist = Q.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
                if maze[nr][nc] == 3:
                    return 1
                elif maze[nr][nc] == 0:
                    Q.append((nr, nc, dist + 1))
                    visit[nr][nc] = 1

    return 0


T = 10
N = 16
for _ in range(T):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    # bfs를 실행하여 도착 지점(3)에 갈 수 있는지 확인, 가능하면 1리턴, 불가능하면 0리턴
    visit = [[0] * N for _ in range(N)]
    result = bfs(1, 1, 0) #행, 열, 출발지로부터 거리
    print('#{} {}'.format(tc, result))