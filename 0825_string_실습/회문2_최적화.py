import sys

sys.stdin = open('회문2.txt')

T = 10
N = 100
for t in range(T):
    tc = int(input())
    board = [input() for _ in range(N)]
    # print(tc)
    # print(board)

    max_pal_len = 0

    # 회문 탐색
    for i in range(N):  # 몇번째 행 또는 열인지
        # print(board[i])
        for j in range(N):  # 시작점
            for k in range(N - 1, j - 1, -1):  # 끝점

                # 가로회문 탐색
                for l in range((k - j + 1) // 2): # 비교해야할 횟수
                    if board[i][j + l] != board[i][k - l]:
                        break

                else:
                    # print(board[i][j:k+1])
                    row_pal_len = len(board[i][j:k + 1])
                    if row_pal_len > max_pal_len:
                        max_pal_len = row_pal_len

                # 세로회문 탐색
                for l in range((k - j + 1) // 2):  # 비교해야할 횟수
                    if board[j + l][i] != board[k - l][i]:
                        break

                else:
                    col_pal = ""
                    for m in range(j, k + 1):
                        col_pal += board[m][i]
                    # print(col_pal)

                    col_pal_len = len(col_pal)
                    if col_pal_len > max_pal_len:
                        max_pal_len = col_pal_len

    print("#{} {}".format(tc, max_pal_len))