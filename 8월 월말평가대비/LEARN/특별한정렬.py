import sys
sys.stdin = open('특별한정렬.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(N, numbers)

    for i in range(N-1):
        idx = i
        for j in range(i, N):
            if i % 2 == 0: # 짝수번째이면 큰수
                if numbers[j] > numbers[idx]:
                    idx = j
            else: # 홀수번째이면 작은수
                if numbers[j] < numbers[idx]:
                    idx = j
        numbers[i], numbers[idx] = numbers[idx], numbers[i]

    print("#{}".format(tc), end=" ")
    for i in range(10):
        print(numbers[i], end=" ")
    print()


