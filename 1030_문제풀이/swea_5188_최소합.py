import sys
sys.stdin = open('swea_5188_최소합.txt')

# 오른쪽, 아래
dr = [0, 1]
dc = [1, 0]

def dfs(r, c, cursum):
    global min_num

    if min_sum < cursum:
        return

    if (r, c) == (N - 1, N - 1):
        if min_sum > cursum:
            min_sum = cursum
        return

    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, cursum + board[nr][nc])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(board)
    # 시작 : (0, 0) / 종료 : (N - 1 , N - 1)

    min_num = 10 * (N)
    dfs(0, 0, board[0][0])

    print('#{} {}'.format(tc, min_num))