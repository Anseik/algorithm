T = 10
N = 100

for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    matrix = [[0] * 102 for _ in range(102)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            matrix[i+1][j+1] = arr[i][j]
            if matrix[i+1][j+1] == 2:
                a = j+1

    for i in range(99, -1, -1):
        if matrix[i][a+1] == 1:
            while True:
                a += 1
                if matrix[i][a+1] != 1:
                    break

        elif matrix[i][a-1] == 1:
            while True:
                a = a - 1
                if not matrix[i][a-1]:
                    break

    print('#{} {}'.format(tc, a-1))