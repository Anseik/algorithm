import sys
sys.stdin = open('달팽이.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    board = [[0] * N for _ in range(N)]
    # print(board)

    #우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = 0
    c = 0
    d = 0
    num = 1

    while num <= N*N:
        if 0 <= r < N and 0 <= c < N and board[r][c] == 0:
            board[r][c] = num
            num += 1
        else:
            # 원위치
            r -= dr[d]
            c -= dc[d]
            d = (d + 1) % 4

        r += dr[d]
        c += dc[d]

    print("#{}".format(tc))
    for row in board:
        print(*row)