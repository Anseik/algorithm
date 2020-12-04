import sys
sys.stdin = open('특별한 정렬.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(N)
    # print(numbers)
    for i in range(0, N-1):
        if i % 2 == 0:
            # 최대값을 선택정렬
            max_idx = i
            for j in range(i+1, N):
                if numbers[j] > numbers[max_idx]:
                    max_idx = j
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]

        else:
            # 최소값을 선택정렬
            min_idx = i
            for k in range(i+1, N):
                if numbers[k] < numbers[min_idx]:
                    min_idx = k
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    print('#%d' %tc, end=" ")
    for l in range(10):
        print(numbers[l], end=" ")
    print()
