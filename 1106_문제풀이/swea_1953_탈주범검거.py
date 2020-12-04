import sys
sys.stdin = open('swea_1953_탈주범검거.txt')

# 구조물 타입 번호별 연결 정보(상 하 좌 우)
dir_dict = {
    1: (1, 1, 1, 1), 2: (1, 1, 0, 0), 3: (0, 0, 1, 1), 4: (1, 0, 0, 1),
    5: (0, 1, 0, 1), 6: (0, 1, 1, 0), 7: (1, 0, 1, 0)
}

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(r, c):
    global cnt
    Q = [(r, c, 1)]
    visit[r][c] = 1

    while Q:
        cr, cc, ct = Q.pop(0)
        if ct == L:
            break
        cd = dir_dict[arr[cr][cc]]
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and arr[nr][nc]:
                nd = dir_dict[arr[nr][nc]]
                if (d == 0 and cd[0] and nd[1]) or (d == 1 and cd[1] and nd[0]) or (d == 2 and cd[2] and nd[3]) or (d == 3 and cd[3] and nd[2]):
                    Q.append((nr, nc, ct + 1))
                    visit[nr][nc] = 1
                    cnt += 1

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 1
    visit = [[0] * M for _ in range(N)]
    bfs(R, C)

    print('#{} {}'.format(tc, cnt))