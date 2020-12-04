import sys
sys.stdin = open('BOJ_10163_색종이.txt')

T = 1
L = 101
for tc in range(1, T + 1):
    N = int(input())
    board = [[0] * L for _ in range(L)]

    num = 0
    for i in range(N):
        sc, sr, width, height = map(int, input().split())
        # print(sr, sc, width, height)

        num += 1
        for r in range(sr, sr + height):
            for c in range(sc, sc + width):
                board[r][c] = num
    # print(board)

    result = []
    for k in range(1, N + 1):
        cnt = 0
        for m in range(L):
            for n in range(L):
                if board[m][n] == k:
                    cnt += 1
        result.append(cnt)

    for ans in result:
        print(ans)


