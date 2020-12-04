import sys
sys.stdin = open('boj_1036_36진수.txt')


def base32_to_decimal(c):
    num = ord(c)
    if 48 <= num <= 57:
        return num - ord('0')
    elif 65 <= num <= 90:
        return num - ord('A') + 10


def decimal_to_base32(n):
    if n == 0:
        return '0'

    target = n
    ret = []
    while target > 0:
        rest = target % 36
        ret.insert(0, rest)
        target //= 36


    base32 = ''
    for t in range(len(ret)):
        if 0 <= ret[t] <= 9:
            base32 += chr(ret[t] + ord('0'))
        elif 10 <= ret[t] <= 35:
            base32 += chr(ret[t] + ord('A') - 10)
    return base32


# 입력부
N = int(input())
numbers = []
for i in range(N):
    num32 = input()
    l = len(num32)
    for j in range(l):
        numbers.append((l - 1 - j, num32[j]))
# print(numbers)
K = int(input())

numbers.sort()
# print(numbers)
# print(N, K)
L = len(numbers)

# 바꿀 숫자를 K개 선택(자리수가 큰것, 자리수가 같으면 숫자가 작은것), 계수가 0이면 선택하지 않는다.
select = [0] * L
change = []
while len(change) < K:
    tp = 0
    tn = '1'
    # print(tp, tn)
    idx = 0
    for j in range(L):
        # 자리수가 큰것을 선택
        if numbers[j][0] > tp and not select[j] and numbers[j][1] > '0':
            tp = numbers[j][0]
            tn = numbers[j][1]
            idx = j
        # 자리수가 같으면 숫자가 작은것을 선택
        elif numbers[j][0] == tp and '0' < numbers[j][1] < tn and not select[j]:
            tp = numbers[j][0]
            tn = numbers[j][1]
            idx = j
    select[idx] = 1
    # 바꿀 숫자가 중복되지 않도록 한다.
    if not numbers[idx][1] in change:
        change.append(numbers[idx][1])
# print(change)

# 선택된 숫자를 모두 Z로 바꾼다.
new_numbers = []
for k in range(L):
    if numbers[k][1] in change:
        new_numbers.append((numbers[k][0], 'Z'))
    else:
        new_numbers.append(numbers[k])
# print(new_numbers)

deci_sum = 0
for d in range(L):
    # print(new_numbers[d][1])
    deci = base32_to_decimal(new_numbers[d][1])
    # print(36 ** new_numbers[d][0])
    # print(deci)
    deci_sum += (deci * (36 ** new_numbers[d][0]))
# print(deci_sum)

result = decimal_to_base32(deci_sum)
print(result)

