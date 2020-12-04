import sys
sys.stdin = open('구간합.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # print(list_info)
    # print(numbers)

    results = []
    for i in range(N - M + 1):
        sum = 0
        for j in range(i, i + M):
            sum += numbers[j]
        results.append(sum)

    print(results)

    max_result = results[0]
    min_result = results[0]
    for result in results:
        if result > max_result:
            max_result = result

    for result in results:
        if result < min_result:
            min_result = result


    # print('#%d' %tc, max_result - min_result)