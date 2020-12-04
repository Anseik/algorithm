def find_palindrome(board):
    result = "" #회문을 찾으면 반환하기 위한 변수
    # 행우선순회
    for i in range(N):
        for j in range(N-M+1):
            # 회문검사
            for k in range(M//2):
                if board[i][j+k] != board[i][j+M-1-k]:
                    break # 회문이 아님
            else: # 회문 찾음
                result = board[i][j:j+M]
                return result

    # 열우선순회
    for i in range(N):
        for j in range(N-M+1):
            # 회문검사
            for k in range(M//2):
                if board[j+k][i] != board[j+M-1-k][i]:
                    break # 회문이 아님
            else: # 회문 찾음
                for x in range(j, j+M):
                    result += board[x][i]
                return result



import sys
sys.stdin = open('회문.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)

    board = [input() for _ in range(N)]
    # print(board)

    result = find_palindrome(board)


    print("#{} {}".format(tc, result))