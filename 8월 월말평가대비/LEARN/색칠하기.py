import sys
sys.stdin = open('색칠하기.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # print(N)
    board = [[0] * 10 for _ in range(10)]
    # print(board)

    cnt = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # print(r1, c1, r2, c2, color)
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                board[r][c] += color
                if board[r][c] == 3:
                    cnt += 1

    # print(board)
    print("#{} {}".format(tc, cnt))



