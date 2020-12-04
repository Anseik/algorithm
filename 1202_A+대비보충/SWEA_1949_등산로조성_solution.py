import sys
sys.stdin = open('SWEA_1949_등산로조성.txt')

def f(i, j, c, s, N, K):
    global maxV
    if maxV < s + 1:
        maxV = s + 1

    visited[i][j] = 1
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = pass


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # print(N, K)
    # print(arr)

    # 가장 높은 봉우리의 높이를 찾고
    max_h = 0
    for r in range(N):
        for c in range(N):
            if max_h < arr[r][c]:
                max_h = arr[r][c]

    maxV = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_h:
                f(i, j, 1, 0, N, K)

    print('#{} {}'.format(tc, maxV))