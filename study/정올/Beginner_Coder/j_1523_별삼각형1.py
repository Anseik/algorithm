import sys
for line in sys.stdin:
    n, m = map(int, line.rstrip().split())
    if not ((1 <= n <= 100) and (1 <= m <= 3)):
        print('INPUT ERROR!')

    else:
        # 종류1
        if m == 1:
            arr = [[' '] * n for _ in range(n)]
            r = 0
            for i in range(n):
                r += 1
                for j in range(r):
                    arr[i][j] = '*'

            for p in arr:
                for o in p:
                    print(o, end='')
                print()

        # 종류2
        elif m == 2:
            arr = [[' '] * n for _ in range(n)]
            r = n + 1
            for i in range(n):
                r -= 1
                for j in range(r):
                    arr[i][j] = '*'

            for p in arr:
                for o in p:
                    print(o, end='')
                print()

        # 종류3
        elif m == 3:
            arr = [[' '] * (2 * n - 1) for _ in range(n)]
            # print(arr)

            r = 0
            k = 1
            for c in range((2 * n - 1) // 2, -1, -1):
                for j in range(2 * k - 1):
                    arr[r][c + j] = '*'
                r += 1
                k += 1

            for p in arr:
                for o in p:
                    print(o, end='')
                print()


