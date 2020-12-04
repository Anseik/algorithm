import sys
import string
sys.stdin = open('boj_1036_36진수.txt')

base32_string = string.digits + string.ascii_uppercase
base32_to_deci = {base32: base10 for base10, base32 in enumerate(base32_string)}
# deci_to_base32 = {base10: base32 for base10, base32 in enumerate(base32_string)}

# print(base32_to_deci)
# print(deci_to_base32)

# def base32_to_decimal(c):
#     num = ord(c)
#     if 48 <= num <= 57:
#         return num - ord('0')
#     elif 65 <= num <= 90:
#         return num - ord('A') + 10
#
#
def decimal_to_base32(n):
    if n == 0:
        return '0'

    target = n
    ret = ''
    while target > 0:
        rest = target % 36
        if 0 <= rest <= 9:
            ret = chr(rest + ord('0')) + ret
        elif 10 <= rest <= 35:
            ret = chr(rest + ord('A') - 10) + ret
        target //= 36
    return ret


# 입력부
N = int(input())
numbers = [0] * 36 # 인덱스 : 계수 / 값 : 전개식(36^0 + 36^1 + ... + 36^49)
# print(numbers)
for i in range(N):
    tmp = input()
    l = len(tmp)
    for j in range(l):
        ind = l - 1 - j
        idx = base32_to_deci[tmp[j]]
        numbers[idx] += (36 ** ind)
# print(numbers)
K = int(input())

result = 0
add_sum = []
for eff in range(36):
    result += eff * numbers[eff]
    add_sum.append((35 - eff) * numbers[eff])

add_sum.sort(reverse=True)
for j in range(K):
    result += add_sum[j]

# print(result)

ans = decimal_to_base32(result)
print(ans)