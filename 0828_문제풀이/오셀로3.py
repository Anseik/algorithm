import sys
sys.stdin = open('SWEA_4615_재미있는오셀로게임_안세익.txt')

# 델타 방향으로 바꿀 돌들이 있는지 확인 하는 함수(같은 색깔 돌 사이에 다른 색깔 돌이 있는지 확인)
def between(nr, nc):
    while 0 < nr <= N and 0 < nc <= N:
        # while문을 돌면서 같은 색깔 돌 사이에 다른 색 돌이 어디 있는지 저장
        if board[nr][nc] == 0: # 0이 나오면 같은 색 사이에 다른 색깔 돌이 놓인 경우가 아니므로 False
            return False
        elif board[nr][nc] != 0 and board[nr][nc] != color: # 바꿔야 될 돌을 찾아 위치를 저장
            change.append((nr, nc)) # change에 일단 추가는 하지만 사이에 있는 돌이 아니면 버려진다.
        elif board[nr][nc] == color: # 같은 색 돌 사이에 바꿔야 할 돌이 있다면
            return True

        # 함수가 끝나지 않으면 델타를 증가시키며 탐색을 계속한다.
        nr = nr + dr[j]
        nc = nc + dc[j]

    return False # 위에서 return을 한번도 못 만나면 즉 시작부터 끝까지 같은 색 돌만 놓여있으면 False를 반환

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

        # 팔방 순회하면서 바꿀 돌의 위치를 저장한다.
        for j in range(len(dr)):
            nr = r + dr[j]
            nc = c + dc[j]
            change = list()  # 색상을 바꿀 돌의 좌표를 저장 하는 리스트

            if between(nr, nc): # 해당 델타 방향으로 색깔을 바꿀 돌들이 있다면
                for k in range(len(change)):
                    kr, kc = change[k]
                    board[kr][kc] = color

    # print(board)
    black = 0
    white = 0
    for i in range(N+1):
        black += board[i].count(1)
        white += board[i].count(2)

    print("#{} {} {}".format(tc, black, white))