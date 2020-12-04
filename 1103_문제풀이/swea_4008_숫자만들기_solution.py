import sys
sys.stdin = open('swea_4008_숫자만들기_solution.txt')

# 연산자 순서의 모든 경우의 수 구하기
def solve(idx, order):
    global max_num, min_num
    if idx >= N - 1:
        # 0 : 더하기 / 1 : 빼기 / 2 : 곱하기 / 3: 나누기
        tmp = numbers[0]
        for j in range(N - 1):
            if order[j] == 0:
                tmp += numbers[j + 1]
            elif order[j] == 1:
                tmp -= numbers[j + 1]
            elif order[j] == 2:
                tmp *= numbers[j + 1]
            elif order[j] == 3:
                tmp = int(tmp / numbers[j + 1])
        max_num = max(max_num, tmp)
        min_num = min(min_num, tmp)
        return

    # 사용가능한 연산자 살펴보기
    for i in range(4):
        if opers[i]:
            order[idx] = i
            opers[i] -= 1 # 사용한 연산자의 개수를 1 감소
            solve(idx + 1, order)
            opers[i] += 1 # 재귀호출이 끝나면 다시 사용할 수 있도록 1 증가


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    # print(N)
    # print(opers)
    # print(numbers)
    order = [-1] * (N - 1)
    max_num = -100000000
    min_num = 100000000
    solve(0, order)
    ans = max_num - min_num
    print('#{} {}'.format(tc, ans))
