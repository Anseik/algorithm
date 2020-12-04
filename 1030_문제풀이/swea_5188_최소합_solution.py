import sys
sys.stdin = open('swea_5188_최소합.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0xfffffffff
    def dfs(x, y, dist): # 현재 위치(행-x, 열-y)
        global ans
        if dist >= ans:
            return
        if x == N - 1 and y == N - 1:
            ans = min(ans, dist)
        else:
            if x + 1 < N: # 아래
                dfs(x + 1, y, dist + arr[x + 1][y])
            if y + 1 < N: # 오른쪽
                dfs(x, y + 1, dist + arr[x][y + 1])

    dfs(0, 0, arr[0][0])
    print('#{} {}'.format(tc, ans))