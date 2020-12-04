N = 8
R = 4
C = 5
board = [[0] * (N+1) for _ in range(N+1)]

# 상 상우 우 하우 하 하좌 좌 상좌
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(8):
    nr = R
    nc = C
    # 한 방향에 대해서 전부 1로 바꿔주고 나서
    # 다음 방향에 대해서 1로 바꿔주라
    # nr, nc에 현재 방향의 델타를 계속 더해주면서 영역이 끝나기 전까지 증가

    while True:
        # 범위가 벗어날때까지 nr과 nc를 현재 방향으로 증가
        if 0 < nr <= N and 0 < nc <= N:
            board[nr][nc] = 1
            nr += dr[i]
            nc += dc[i]
        else:
            break

print(board)
