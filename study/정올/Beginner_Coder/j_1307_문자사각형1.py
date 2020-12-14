import sys
for line in sys.stdin:
    n = int(line)
    arr = [[''] * n for _ in range(n)]
    # print(arr)

    num = ord('A')
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if num > ord('Z'):
                num = ord('A')
            arr[j][i] = chr(num)
            num += 1

    for a in arr:
        print(*a)