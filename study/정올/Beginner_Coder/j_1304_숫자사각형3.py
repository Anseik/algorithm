import sys
for line in sys.stdin:
    n = int(line)
    arr = [[0] * n for _ in range(n)]

    num = 1
    for i in range(n):
        for j in range(n):
            arr[j][i] = num
            num += 1

    for a in arr:
        print(*a)

