import sys
sys.stdin = open('SWEA_4615_재미있는오셀로게임_안세익.txt')
# 8방 델타 이용, while문

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    board = [[0] * (N+1) for _ in range(N+1)]
    # print(board)

    st = N // 2
    board[st][st] = board[st+1][st+1] = 2
    board[st][st+1] = board[st+1][st] = 1
    # print(board)

    # 델타 이용한 순회
    # 상 상우 우 하우 하 하좌 좌 상좌
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(M): # 플레이어가 돌을 두는 횟수 만큼 반복
        c, r, color = map(int, input().split())
        board[r][c] = color # 돌을 둔다.
        # print(board)

        # 놓은 돌에서 팔방으로 순회하면서 같은 색의 돌을 찾고 찾으면 다시 돌아오면서 다른 색 돌을 같은 색으로 바꾼다.

        for j in range(len(dr)):
            nr = r + dr[j]
            nc = c + dc[j]
            change = list() # 색상을 바꿀 돌의 좌표를 저장 하는 리스트
            while 0 < nr  <= N and 0 < nc <= N and board[nr][nc] != color:
                # while문을 돌면서 다른 색이 어디 있는지 저장
                if board[nr][nc] != 0:
                    change.append((nr, nc))
                nr = nr + dr[j]
                nc = nc + dc[j]

            if 0 < nr  <= N and 0 < nc <= N and board[nr][nc] == color: # 같은 색돌을 찾은 경우만
                for k in range(len(change)):
                    kr, kc = change[k]
                    board[kr][kc] = color

            # 델타 방향에 같은 색 돌이 있는지 먼저 찾는게 어떨까?



    # print(board)
    black = 0
    white = 0
    for i in range(N+1):
        black += board[i].count(1)
        white += board[i].count(2)

    print("#{} {} {}".format(tc, black, white))
    # 정가운데 배치하기??
    # (2, 3)은 열이 2, 행이 3을 뜻함
