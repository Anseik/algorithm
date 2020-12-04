import sys
sys.stdin = open('회문.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)

    board = [input() for _ in range(N)]
    # print(board)

    result = ""
    # 가로 회문 탐색
    for i in range(N): # 몇번째 행 또는 열인지
        # print(board[i])
        for j in range(N-M+1): # 시작점
            # 가로 회문 탐색
            for k in range(M // 2): # 비교해야할 횟수
                if board[i][j+k] != board[i][j+M-k-1]:
                    break

            else:
                result = board[i][j:j+M]

            # 세로 회문 탐색
            for k in range(M // 2): # 비교해야할 횟수
                if board[j+k][i] != board[j+M-k-1][i]:
                    break

            else:
                for l in range(M):
                    result += board[j+l][i]

    print("#{} {}".format(tc, result))