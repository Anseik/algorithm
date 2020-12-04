import sys
sys.stdin = open('swea_5186_이진수2_solution.txt')

def decimal_to_binary(num):
    result = ''
    cnt = 0
    while num:
        if cnt > 12:
            result = 'overflow'
            break
        tmp = num * 2
        if tmp >= 1:
            result += '1'
            tmp = tmp - 1
        else:
            result += '0'
        num = tmp
        cnt += 1

    return result


T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    result = decimal_to_binary(N)
    print('#{} {}'.format(tc, result))