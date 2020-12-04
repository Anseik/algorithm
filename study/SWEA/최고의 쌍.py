import sys
sys.stdin = open('최고의 쌍.txt')

def comb(selected, idx, cnt):
    if cnt == 2:
        multiply = 1
        for i in range(N):
            if selected[i] == 1:
                multiply *= numbers[i]
        result.append(str(multiply))
        return

    if idx == N:
        return

    selected[idx] = 1
    comb(selected, idx + 1, cnt + 1)
    selected[idx] = 0
    comb(selected, idx + 1, cnt)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(N)
    # print(numbers)

    selected = [0] * (N)
    # print(selected)

    result = []
    comb(selected, 0, 0)
    # print(result)

    filter = []
    for num in result:
        com = int(num[0])
        for i in range(1, len(num)):
            if com + 1 != int(num[i]):
                break
            else:
                com += 1
        else:
            filter.append(int(num))
    # print(filter)
    # 모듈러 연산으로 1씩 줄어드는지 확인하기

    answer = -1
    for value in filter:
        if value > answer:
            answer = value

    print("#{} {}".format(tc, answer))