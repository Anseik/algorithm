import sys
sys.stdin = open('회문.txt')


def pal_check(board):
    pal = ""
    for i in range(N): #행 또는 열
        for j in range(N-M+1): # 시작위치
            # 행 회문검사
            for k in range(M//2):
                if board[i][j + k] != board[i][j + M - k - 1]:
                    break
            else:
                pal += board[i][j:j+M]
                return pal

            # 열 회문검사
            for k in range(M // 2):
                if board[j + k][i] != board[j + M - k - 1][i]:
                    break
            else:
                for l in range(M):
                    pal += board[j+l][i]
                return pal

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    # print(N, M)
    # print(board)
    result = pal_check(board)

    print("#{} {}".format(tc, result))