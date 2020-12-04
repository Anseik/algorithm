for _ in range(10):
    #테스트케이스 번호
    tc = int(input())

    #2차원배열 입력받기
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_value = 0

    #각 행의 합
    for i in range(100):
        sum_v = 0
        for j in range(100):
            sum_v += arr[i][j]
        if sum_v > max_value:
            max_value = sum_v

    # 각 열의 합
    for j in range(100):
        sum_v = 0
        for i in range(100):
            sum_v += arr[i][j]
        if sum_v > max_value:
            max_value = sum_v

    # 대각선 2개의 합

    # 오른쪽 아래로 내려가는 대각선
    sum_v = 0
    for i in range(100):
        sum_v += arr[i][i]
    if sum_v > max_value:
        max_value = sum_v

    # 왼쪽 아래로 내려가는 대각선
    a, b = 0, 99
    sum_v = 0
    for _ in range(100):
        sum_v += arr[a][b]
        a += 1
        b -= 1
    if sum_v > max_value:
        max_value = sum_v

    print('#{} {}'.format(tc, max_value))