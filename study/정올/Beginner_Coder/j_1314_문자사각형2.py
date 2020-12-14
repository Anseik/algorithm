import sys
for line in sys.stdin:
    n = int(line.rstrip())
    # print(n)
    arr = [[''] * n for _ in range(n)]
    # print(arr)

    num = ord('A')
    for c in range(n):
        if c % 2 == 0:
            for r in range(n):
                if num > ord('Z'):
                    num = ord('A')
                arr[r][c] = chr(num)
                num += 1
        else:
            for r in range(n - 1, -1, -1):
                if num > ord('Z'):
                    num = ord('A')
                arr[r][c] = chr(num)
                num += 1

    for a in arr:
        print(*a)
