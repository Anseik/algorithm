import sys
sys.stdin = open('Sum.txt')

T = 10
N = 100
for t in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    result = 0
    dia1_sum = 0 # 좌상-우하
    dia2_sum = 0 # 우상-좌하
    for r in range(N):
        r_sum = 0
        c_sum = 0
        for c in range(N):
            r_sum += arr[r][c]
            c_sum += arr[c][r]
            if r == c:
                dia1_sum += arr[r][c]
            if r + c == N - 1:
                dia2_sum += arr[r][c]

        if r_sum > result:
            result = r_sum
        if c_sum > result:
            result = c_sum

    if dia1_sum > result:
        result = dia1_sum
    if dia2_sum > result:
        result = dia2_sum


    print("#{} {}".format(tc, result))