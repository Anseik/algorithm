import sys
sys.stdin = open('구간합.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # print(N, M)
    # print(numbers)

    number_sum = list()
    for i in range(N-M+1):
        tmp = 0
        for j in range(i, i+M):
            tmp += numbers[j]
        number_sum.append(tmp)

    # print(number_sum)

    max_num = number_sum[0]
    min_num = number_sum[0]
    for k in range(len(number_sum)):
        if number_sum[k] > max_num:
            max_num = number_sum[k]
        if number_sum[k] < min_num:
            min_num = number_sum[k]

    result = max_num - min_num

    print("#{} {}".format(tc, result))


