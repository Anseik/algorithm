import sys
for line in sys.stdin:
    n = int(line.rstrip())
    # print(n)
    arr = [[' '] * n for _ in range(n)]
    # print(arr)

    num = ord('A')
    for i in range(n):
        k = n - 1
        for j in range(i, n):
            if num > ord('Z'):
                num = ord('A')
            arr[j][k] = chr(num)
            num += 1
            k -= 1
    # print(arr)

    for a in arr:
        print(*a)
