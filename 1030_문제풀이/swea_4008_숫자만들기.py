import sys
sys.stdin = open('swea_4008_숫자만들기.txt')

cals_dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: int(x / y)
}

def calculation(idx, curnum):
    global min_num, max_num
    if idx == N:
        min_num = min(min_num, curnum)
        max_num = max(max_num, curnum)
        return
    for o in range(4):
        if ope[o]:
            ope[o] -= 1
            tmp = cals_dict[cals[o]](curnum, numbers[idx])
            calculation(idx + 1, tmp)
            ope[o] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # idx : 0, 1, 2, 3
    # ope : +, -, *, /
    ope = list(map(int, input().split()))
    cals = ['+', '-', '*', '/']
    numbers = list(map(int, input().split()))

    min_num = 100000000
    max_num = -100000000
    calculation(1, numbers[0])
    # print(min_num, max_num)

    ans = max_num - min_num
    print('#{} {}'.format(tc, ans))


    # 연산자를 사용할때마다 값을 -- 사용이 끝나면 ++
    # 현재까지 계산된 결과를 매개변수 curnum에 저장
    # min_num, max_num에 연산결과 최대, 최소 값을 저장