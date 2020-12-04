import sys
sys.stdin = open('sum.txt')

T = 10
for tc in range(1, T+1):
    tn = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    N = len(arr)
    M = len(arr[0])

    max_num = 0
    dia1_sum = 0
    dia2_sum = 0
    for r in range(N):
        row_sum = 0
        col_sum = 0
        for c in range(M):
            row_sum += arr[r][c]
            col_sum += arr[c][r]
            if r == c:
                dia1_sum += arr[r][c]
            if (r + c) == (N - 1):
                dia2_sum += arr[r][c]

        if row_sum > max_num:
            max_num = row_sum
        if col_sum > max_num:
            max_num = col_sum

    if dia1_sum > max_num:
        max_num = dia1_sum
    if dia2_sum > max_num:
        max_num = dia2_sum
            
    print('#%d' % tn, max_num)
