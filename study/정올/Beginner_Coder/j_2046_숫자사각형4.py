import sys
for line in sys.stdin:
    n, m = map(int, line.strip().split())
    # print(n, m)
    arr = [[0] * n for _ in range(n)]
    # print(arr)

    # 종류1
    if m == 1:
        num = 1
        for i in range(n):
            for j in range(n):
               arr[i][j] = num
            num += 1

    # 종류2
    elif m == 2:
        for i in range(n):
            # 짝수 행
            if i % 2 == 0:
                num = 1
                for j in range(n):
                    arr[i][j] = num
                    num += 1
            # 홀수 행
            else:
                num = n
                for j in range(n):
                    arr[i][j] = num
                    num -= 1

    # 종류3
    elif m == 3:
        st = 1
        for i in range(n):
            for j in range(n):
                arr[i][j] = st * (j + 1)
            st += 1

    # 출력
    for a in arr:
        print(*a)
