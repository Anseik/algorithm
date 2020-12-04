import sys
sys.stdin = open('min_max.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(N)
    # print(numbers)

    max_num = numbers[0]
    min_num = numbers[0]
    for i in range(N):
        if numbers[i] > max_num: max_num = numbers[i]
        if numbers[i] < min_num: min_num = numbers[i]

    result = max_num - min_num

    print("#{} {}".format(tc, result))

