import sys
from collections import defaultdict
sys.stdin = open('boj_1050_물약.txt')

N, M = map(int, input().split())
mat_dict = defaultdict(int)
for i in range(N):
    name, cost = input().split()
    cost = int(cost)
    mat_dict[name] = cost

target = ''
for j in range(M):
    tmp = input()
    idx = tmp.index('=')
    key = tmp[:idx]
    met = tmp[idx + 1:]

    if key == 'LOVE':
        target = tmp
    else:
        val = 0
        multi = 0
        ma = ''
        for m in range(len(met)):
            if '1' <= met[m] <= '9':
                multi = int(met[m])
            elif 'A' <= met[m] <= 'Z':
                ma += met[m]
                if ma in mat_dict:
                    val += (multi * mat_dict[ma])
            elif met[m] == '+':
                multi = 0
                ma = ''

        mat_dict[key] = val

# print(mat_dict)
# print(target)


idx = target.index('=')
key = target[:idx]
met = target[idx + 1:]

result = 0
multi = 0
ma = ''
for m in range(len(met)):
    if '1' <= met[m] <= '9':
        multi = int(met[m])
    elif 'A' <= met[m] <= 'Z':
        ma += met[m]
        if ma in mat_dict:
            result += (multi * mat_dict[ma])
    if met[m] == '+' or m == len(met) - 1:
        if ma not in mat_dict:
            result = -1
            break
        else:
            multi = 0
            ma = ''

if result > 1000000000:
    print(1000000001)
else:
    print(result)




