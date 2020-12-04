import sys
from collections import deque
sys.stdin = open('SWEA_1949_등산로조성.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global max_d
    Q = deque()
    Q.append((r, c, 1))
    while Q:
        cr, cc, cd = Q.popleft()
        if max_d < cd:
            max_d = cd
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] < arr[cr][cc]:
                    Q.append((nr, nc, cd + 1))

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N, K)
    # print(arr)

    # 가장 높은 봉우리의 높이를 찾고
    max_h = 0
    for r in range(N):
        for c in range(N):
            if max_h < arr[r][c]:
                max_h = arr[r][c]
    # 그 높이에 해당하는 위치를 저장한다.
    sp = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == max_h:
                sp.append((r, c))
    # print(max_h)
    # print(start_points)

    # 모든 지점을 순회하며 1부터 K까지 깍아보면서 탐색을 한다.
    max_d = 0
    for k in range(K + 1):
        for y in range(N):
            for x in range(N):
                # 한 지점을 k만큼 깍아 두고 탐색을 시작한다.
                arr[y][x] = arr[y][x] - k

                # 가장 높은 봉우리들에서 bfs탐색
                for i in range(len(sp)):
                    sr, sc = sp[i]
                    # print(sr, sc)
                    bfs(sr, sc)

                # 다음 탐색을 위해 원상복구
                arr[y][x] = arr[y][x] + k

    print('#{} {}'.format(tc, max_d))