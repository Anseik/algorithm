import sys
sys.stdin = open('BOJ_2669_직사각형.txt')

T = 1
for tc in range(1, T + 1):
    boards = [[0] * 101 for _ in range(101)]
    # print(boards)
    for i in range(4):
        # x1, y1 : 왼쪽 아래 꼭지점의 x,y 좌표
        # x2, y2 : 오른쪽 위 꼭지점의 x,y 좌표
        x1, y1, x2, y2 = map(int, input().split())
        # print(x1, y1, x2, y2)
        c1, r1, c2, r2 = x1, 100 - y1, x2, 100 - y2
        # print(c1, r1, c2, r2)
        row_size = r1 - r2
        col_size = c2 - c1
        for r in range(r2, r2 + row_size):
            for c in range(c1, c1 + col_size):
                boards[r][c] = 1

    # print(boards)
    area = 0
    for m in range(101):
        for n in range(101):
            if boards[m][n] == 1:
                area += 1
    print(area)
