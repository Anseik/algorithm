import sys
sys.stdin = open('boj_19532_수학은.txt')

a, b, c, d, e, f = map(int, input().split())
# print(a, b, c, d, e, f)
result = []
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            result.append(x)
            result.append(y)
print(*result)

