import sys
import string
sys.stdin = open('swea_5185_이진수_solution.txt')


change_dict = {c: deci for deci, c in enumerate(string.digits + string.ascii_uppercase)}
# print(change_dict)

def deci_to_binary(n):
    target = n
    tmp = ['0'] * 4
    idx = 3
    while target > 0:
        rest = target % 2
        tmp[idx] = str(rest)
        target //= 2
        idx -= 1
    ret = ''.join(tmp)
    return ret


T = int(input())
for tc in range(1, T + 1):
    N, hex = input().split()
    N = int(N)
    # print(N)
    # print(hex)
    result = ''
    for i in range(N):
        num = change_dict[hex[i]]
        # print(num)
        bi = deci_to_binary(num)
        # print(bi)
        result += bi

    print('#{} {}'.format(tc, result))
