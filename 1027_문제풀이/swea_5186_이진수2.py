import sys
sys.stdin = open('swea_5186_이진수2.txt')


T = int(input())
for tc in range(1, T + 1):
    num = float(input())

    result = ''
    deci = 0
    for i in range(1, 13):
        plus = 2 ** (-i)
        next = deci + plus
        if num < next:
            result += '0'
        else:
            deci += plus
            result += '1'
            if num == next:
                break

    else:
        result = 'overflow'

    print('#{} {}'.format(tc, result))

