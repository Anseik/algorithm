import sys
sys.stdin = open('swea_5188_최소합.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 매개변수 : 문제를 식별하는 값
    # 반환값 : 문제의 해
    memo = [[-1] * N for _ in range(N)]
    def minSum(x, y): # 현재 위치(행-x, 열-y)
        # 기저영역
        if x == 0 and y == 0:
            return arr[0][0]

        if memo[x][y] != -1:
            return memo[x][y]

        # 위에서 오는 경우, 왼쪽에서 오는 경우
        up = left = 0xfffffff
        if x != 0:
            up = minSum(x - 1, y)
        if y != 0:
            left = minSum(x, y -1)
        memo[x][y] = min(up, left) + arr[x][y]
        return memo[x][y]

    ans = minSum(N - 1, N - 1)
    print('#{} {}'.format(tc, ans))