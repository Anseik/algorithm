import sys
sys.stdin = open('회문2.txt')

def pal_check(board):
    max_pal = 0
    for i in range(N): #행 또는 열
        for j in range(N): # 시작위치
            for m in range(N-1, j-1, -1): # 종료 위치
                # 행 회문검사
                row_pal = ""
                for k in range((m - j + 1) // 2):
                    if board[i][j + k] != board[i][m - k]:
                        break
                else:
                    row_pal += board[i][j:m+1]
                    if len(row_pal) > max_pal:
                        max_pal = len(row_pal)


                # 열 회문검사
                col_pal = ""
                for k in range((m - j + 1) // 2):
                    if board[j + k][i] != board[m - k][i]:
                        break
                else:
                    for l in range(j, m+1):
                        col_pal += board[l][i]
                    if len(col_pal) > max_pal:
                        max_pal = len(col_pal)

    return max_pal


T = 10
N = 100
for t in range(1, T+1):
    tc = int(input())
    board = [input() for _ in range(N)]
    # print(board)
    result = pal_check(board)

    print("#{} {}".format(tc, result))