import sys
for line in sys.stdin:
    n, m = map(int, line.strip().split())
    arr = [[0] * m for _ in range(n)]
    # print(arr)

    num = 1
    for i in range(n):
        # 짝수행
        if i % 2 == 0:
            for j in range(0, m):
                arr[i][j] = num
                num += 1

        # 홀수행
        else:
            for j in range(m - 1, -1, -1):
                arr[i][j] =num
                num += 1

    for a in arr:
        print(*a)

