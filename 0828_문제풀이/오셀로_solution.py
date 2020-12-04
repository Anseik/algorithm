import sys
sys.stdin = open('SWEA_4615_재미있는오셀로게임_안세익.txt')


def init():
    st = N // 2
    board[st][st] = board[st + 1][st + 1] = 2
    board[st][st + 1] = board[st + 1][st] = 1


# 델타 이용한 순회
# 상 상우 우 하우 하 하좌 좌 상좌
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def change(c, r, color):
    # 돌을 놓았을 때 영향을 미치는 곳의 돌색깔 바꾸기
    # 8방향을 검사한다.
    # 영역을 벗어나기 전(또는 빈칸)까지 검사하면서, 나랑 같은 돌이 나올때까지 진행
    # 같은 돌이 나오면, 되돌아 오면서 색깔을 바꾼다.
    board[r][c] = color
    for d in range(8):
        nr = r
        nc = c
        while True:
            nr += dr[d]
            nc += dc[d]
            # nr과 nc가 범위를 벗어나거나 0을 만나면 break
            if nr <= 0 or nr > N or nc <= 0 or nc > N or board[nr][nc] == 0:
                break

            # 범위 내에서(위에서 break가 안걸리면) 나랑 같은 색깔의 돌을 찾았으면
            if board[nr][nc] == color:
                # 그 위치부터 원래 위치까지 되돌아 오면서 내 색깔로 바꿔줌
                while not (nr == r and nc == c): # 원래 자리로 돌아올때까지
                    nr -= dr[d]
                    nc -= dc[d]
                    board[nr][nc] = color
                break # 바깥쪽 while 종료


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    board = [[0] * (N+1) for _ in range(N+1)]
    # 초기돌 놓기
    init()

    for i in range(M):
        c, r, color = map(int, input().split())
        # print(c, r, color)
        change(c, r, color)

    # print(board)
    b_cnt = 0
    w_cnt = 0
    for row in board:
        b_cnt += row.count(1)
        w_cnt += row.count(2)
    print("#{} {} {}".format(tc, b_cnt, w_cnt))


