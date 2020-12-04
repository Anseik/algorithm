import sys
sys.stdin = open('sum.txt')

T = 10
for tc in range(1, T+1):
    tn = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]

    # 가로합, 세로합, 대각, 역대각
    max_num = [0] * 4

    # 가로합
    for r in range(100):
        row_sum = 0
        for c in range(100):
            row_sum += numbers[r][c]

        if row_sum > max_num[0]:
            max_num[0] = row_sum

    #세로합
    for r in range(100):
        col_sum = 0
        for c in range(100):
            col_sum += numbers[c][r]

        if col_sum > max_num[1]:
            max_num[1] = col_sum

    # 대각, 역대각
    for r in range(100):
        for c in range(100):
            if r == c:
                max_num[2] += numbers[r][c]
            if (r + c) == 99:
                max_num[3] += numbers[r][c]

    result = max_num[0]
    for i in range(len(max_num)):
        if max_num[i] > result:
            result = max_num[i]

    print('#%d' %tc, result)




