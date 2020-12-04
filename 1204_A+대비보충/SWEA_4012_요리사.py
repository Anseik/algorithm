import sys
sys.stdin = open('SWEA_4012_요리사.txt')

def comb(idx, cnt, k):
    global min_d
    if cnt == k:
        ma_A = []
        ma_B = []
        for i in range(N):
            if sel[i] == 1:
                ma_A.append(i)
            else:
                ma_B.append(i)

        food_A = 0
        for i in ma_A:
            for j in ma_A:
                food_A += sy[i][j]

        food_B = 0
        for i in ma_B:
            for j in ma_B:
                food_B += sy[i][j]

        case_d = abs(food_A - food_B)
        min_d = min(min_d, case_d)

        return

    if idx == N:
        return
    sel[idx] = 1
    comb(idx + 1, cnt + 1, k)
    sel[idx] = 0
    comb(idx + 1, cnt, k)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    sy = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(sy)

    # 재료번호를 저장한 리스트와 선택여부를 저장할 리스트 생성
    ma = [num for num in range(N)]
    sel = [0] * N
    # print(ma, sel)

    k = N // 2
    min_d = float('inf')
    comb(0, 0, k)

    print('#{} {}'.format(tc, min_d))