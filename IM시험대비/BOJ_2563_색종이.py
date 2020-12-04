import sys
sys.stdin = open('BOJ_2563_색종이.txt')

T = 1
b_size = 100 # 도화지 크기
p_size = 10 # 색종이 크기
for tc in range(1, T + 1):
    N = int(input())
    boards = [[0] * b_size for _ in range(b_size)]
    # print(N)
    # print(boards)

    for i in range(N):
        left, down = map(int, input().split())
        sr, sc = (b_size - 1) - down, left # 좌측 하단 좌표
        # print(sr, sc)
        for r in range(sr, sr - p_size, -1):
            for c in range(sc, sc + p_size):
                boards[r][c] = 1
    #     print(boards)
    # print(boards)

    area = 0
    for i in range(b_size):
        for j in range(b_size):
            if boards[i][j] == 1:
                area += 1
    print(area)