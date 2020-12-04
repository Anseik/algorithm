import sys
sys.stdin = open('boj_8895_막대배치.txt')

def solve(n, l, r):
    # dp생성
    dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
    # 기저영역
    dp[1][1][1] = 1

    # 높이가 1인 막대 기준으로 생각
    # 높이가 1인 막대가 가장 왼쪽에 있을때 / 가장 오른쪽에 있을때 / 그 외의 경우(n-2가지)

    # i: n / j: l / k: r
    for i in range(2, n + 1):
        for j in range(1, l + 1):
            for k in range(1, r + 1):
                dp[i][j][k] = dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] + ((i - 2) * dp[i - 1][j][k])

    return dp[n][l][r]


T = int(input())
for tc in range(1, T + 1):
    n, l, r = map(int, input().split())
    # print(n, l, r)
    result = solve(n, l, r)
    print(result)