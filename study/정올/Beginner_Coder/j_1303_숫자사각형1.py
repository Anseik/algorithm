import sys
for line in sys.stdin:
    n, m = map(int, line.strip().split())
    # print(n, m)

    num = 1
    for i in range(n):
        for j in range(m):
            print(num, end=" ")
            num += 1
        print()

