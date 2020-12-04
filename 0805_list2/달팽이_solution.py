import sys
sys.stdin = open('달팽이.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    cnt = N * N

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = 0
    c = 0
    d = 0
    num = 1
    while num <= cnt:
    # 횟수가 정해져있으면 for문
    # 횟수가 정해져있지 않으면 while문 사용
        if 0 <= r < N and 0 <= c < N and not arr[r][c]:
            arr[r][c] = num
            num += 1
        else:
            r -= dr[d] # 원위치
            c -= dc[d] # 원위치
            d = (d+1)%4

        r += dr[d]
        c += dc[d]

    for row in arr:
        print(row)
