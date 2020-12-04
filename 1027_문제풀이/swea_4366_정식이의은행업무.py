import sys
import copy
sys.stdin = open('swea_4366_정식이의은행업무.txt')


def binary_to_decimal(tg):
    N = len(tg)
    deci = 0
    for j in range(N):
        if tg[j] == 1:
            deci += 2 ** (N - 1)
        N -= 1
    return deci


def decimal_to_three(deci):
    th2 = []
    target = deci
    while target > 0:
        rest = target % 3
        th2.insert(0, rest)
        target //= 3
    return th2


T = int(input())
for tc in range(1, T + 1):
    bi = list(map(int, input()))
    th = list(map(int, input()))
    # print(bi, th)

    result = 0
    for i in range(1, len(bi)):
        tg = copy.deepcopy(bi)
        if tg[i] == 1:
            tg[i] = 0
        else:
            tg[i] = 1
        deci = binary_to_decimal(tg)
        th2 = decimal_to_three(deci)

        # 길이체크, 다른자리수 체크
        if len(th) == len(th2):
            cnt = 0
            for i in range(len(th)):
                if th[i] != th2[i]:
                    cnt += 1
            if cnt == 1:
                result = deci
                break

    print('#{} {}'.format(tc, result))

