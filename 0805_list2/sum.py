import sys
sys.stdin = open('sum.txt')

T = 10
for tc in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)
    max_sum_list = []

    max_row_sum = 0
    for r in range(len(arr)):
        row_sum = 0
        for c in range(len(arr[r])):
            row_sum += arr[r][c]
        if row_sum > max_row_sum:
            max_row_sum = row_sum
    # print(max_row_sum)
    max_sum_list.append(max_row_sum)

    max_column_sum = 0
    for c in range(len(arr[0])):
        column_sum = 0
        for r in range(len(arr)):
            column_sum += arr[r][c]
        if column_sum > max_column_sum:
            max_column_sum = column_sum
    # print(max_column_sum)
    max_sum_list.append(max_column_sum)

    dia1_sum = 0
    dia2_sum = 0
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if r == c:
                dia1_sum += arr[r][c]
            elif r + c == 99:
                dia2_sum += arr[r][c]
    # print(dia1_sum)
    # print(dia2_sum)
    max_sum_list.append(dia1_sum)
    max_sum_list.append(dia2_sum)

    # print(max_sum_list)
    result = 0
    for max_num in max_sum_list:
        if max_num > result:
            result = max_num

    print('#%d' %tc, result)

