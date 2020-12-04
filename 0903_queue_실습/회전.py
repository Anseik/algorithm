import sys
sys.stdin = open('회전.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # print(N, M)
    # print(numbers)

    for i in range(M):
        numbers.append(numbers.pop(0))

    result = numbers[0]
    print("#{} {}".format(tc, result))

