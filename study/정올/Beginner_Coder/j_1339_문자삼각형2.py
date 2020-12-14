import sys
for line in sys.stdin:
    n = int(line.rstrip())
    # print(n)
    if not ((1 <= n <= 100) and (n % 2 == 1)):
        print('INPUT ERROR')

    else:
        arr = [[' '] * n for _ in range(n)]
        # print(arr)

        num = ord('A')
        for i in range(n // 2, -1, -1):
            k = i
            for j in range(n - 2 * i):
                if num > ord('Z'):
                    num = ord('A')
                arr[k][i] = chr(num)
                num += 1
                k += 1

        for a in arr:
            print(*a)

