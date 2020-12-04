import sys
sys.stdin = open('SWEA_보급로.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input())) for _ in range(N)]

    visit = [[-1] * N for _ in range(N)] # 복구시간이 0인 경우가 있으므로 초기화를 -1로 한다.
    Q = []
    Q.append((0, 0))
    visit[0][0] = 0

    while Q:
        cr, cc = Q.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if visit[nr][nc] == -1:
                    Q.append((nr, nc))
                    visit[nr][nc] = visit[cr][cc] + area[nr][nc]

                # visit[nr][nc]가 -1이 아니면 다른 경로로 해당 위치에 왔었다는 의미
                # 다른 경로로 왔을때와 현재 경로로 왔을때 걸린시간을 비교하여 걸린시간이 적을때만 처리
                elif visit[cr][cc] + area[nr][nc] < visit[nr][nc]:
                    Q.append((nr, nc))
                    visit[nr][nc] = visit[cr][cc] + area[nr][nc]

    result = visit[N - 1][N - 1]
    print("#{} {}".format(tc, result))