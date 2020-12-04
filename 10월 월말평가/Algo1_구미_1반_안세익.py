import sys
sys.stdin = open('Algo1_구미_1반_안세익.txt')

# 배열을 시계방향 90도 회전하는 함수
def turn_90(target):
    ret = [[0] * K for _ in range(K)]
    for r in range(K):
        for c in range(K):
            ret[c][K - 1 - r] = target[r][c]
    return ret


T = int(input())
for tc in range(1, T + 1):
    # N 배열의 크기 / C 회전 각도 / X 시작 열 / Y 시작 행 / K 부분영역 사이즈 / R 출력할 행
    N, C, X, Y, K, R = map(int, input().split())
    # 배열 초기화
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    # 0번 인덱스는 미사용, 값을 채운다.
    for i in range(1, N + 1):
        tmp = list(map(int, input().split()))
        for j in range(1, N + 1):
            arr[i][j] = tmp[j - 1]
    # print(N, C, X, Y, K, R)
    # print(arr)

    # 부분영역이 범위 내에 있는지 체크
    inside = True
    if (Y + K - 1) > N or (X + K - 1) > N:
        inside = False # 부분영역이 범위를 벗어나면 False 차후에 -1로 출력
    # print(inside)

    # 부분영역이 범위 내에 있을 때만 회전
    if inside:
        turn = C // 90 # 배열을 시계방향 90도로 회전시키는 횟수
        # print(turn)

        target = [] # 회전 시킬 배열
        for r in range(Y, Y + K):
            row = []
            for c in range(X, X + K):
                row.append(arr[r][c])
            target.append(row)
        # print(target)

        # 해당 횟수만큼 회전
        for _ in range(turn):
            target = turn_90(target)
        # print(target)

        # 회전 시킨 target을 원배열에 덮어 씌운다.
        for i in range(K):
            for j in range(K):
                arr[Y+i][X+j] = target[i][j]

    # 부분영역이 범위내에 있으면 R행의 합을 출력
    if inside:
        print('#{} {}'.format(tc, sum(arr[R])))
    # 부분영역이 범위내에 있지 않으면 -1을 출력
    else:
        print('#{} {}'.format(tc, -1))





