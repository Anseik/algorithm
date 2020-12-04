# 오셀로 함수 = 하나 돌 놓을 때마다 돌 다 뒤집는 함수
def Othello(y, x, dol):
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(8):
        Y = dy[i]
        X = dx[i]

        # 상대방 돌을 내 돌로 바꾸는 리스트 생성
        dol_change = []

        while True:
            # 주변으로 이동 못할 때 or 돌이 없을 때
            if y + Y < 0 or y + Y >= N or x + X < 0 or x + X >= N or matrix[y + Y][x + X] == 0: break
            # (2) 자기자신과 같은 색의 돌이면
            elif matrix[y + Y][x + X] == dol:
                # 지금까지 저장해둔 상대방돌(위치좌표)를 내 돌로 바꾼다.
                for a, b in dol_change:
                     matrix[a][b] = dol
                # 반복문 중지, 여기까지.
                break
            # (1)상대방 돌이면
            else:
                dol_change.append([y + Y, x + X])

            Y += dy[i]
            X += dx[i]


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]

    # 초기 바둑돌 셋팅
    # 1이 흑돌
    # 2가 백돌
    init_pos = N // 2
    matrix[init_pos - 1][init_pos - 1] = matrix[init_pos][init_pos] = 2
    matrix[init_pos][init_pos - 1] = matrix[init_pos - 1][init_pos] = 1

    for _ in range(M):
        y, x, dol = map(int, input().split())
        # 일단 해당 돌을 놓고,
        matrix[y - 1][x - 1] = dol
        # 돌을 놓을 때마다 오셀로(뒤집는) 함수 호출
        Othello(y - 1, x - 1, dol)

    # 갯수세기
    b_cnt = w_cnt = 0
    for i in matrix:
        b_cnt += i.count(1)
        w_cnt += i.count(2)

    print('#{} {} {}'.format(tc, b_cnt, w_cnt))