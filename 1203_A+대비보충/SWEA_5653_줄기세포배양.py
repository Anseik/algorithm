import sys
from collections import deque
sys.stdin = open('SWEA_5653_줄기세포배양.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def cell_split(X, cr, cc):
    for d in range(4):
        nr = cr + dr[d]
        nc = cc + dc[d]
        # 분열을 할 위치에 아직 세포가 없어야 분열 가능
        if board[nr][nc] == 0:
            # 그 자리에 분열을 하려고 하는 다른 경쟁 세포보다 나의 생명력이 높은지 확인
            for d in range(4):
                ocr = nr + dr[d]
                occ = nc + dc[d]
                # 분열 하려고 하는 다른 세포가 존재하고 그 세포의 생명력이 나의 생명력보다 높으면 break
                other_cell = board[ocr][occ]
                if other_cell:
                    other_X = other_cell[0]
                    other_time = other_cell[2]
                    if other_time == other_X + 1 and other_X > X:
                        break

            # for문이 break되지 않았으면, 즉 내가 nr, nc자리에 분열을 할 수 있으면
            else:
                board[nr][nc] = [X, 1, 0]
                Q.append((nr, nc))


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    init = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M, K)
    # print(init)

    # 배양 용기를 만든다.
    board = [[0] * (2 * K + M) for _ in range(2 * K + N)]
    # print(board)

    # 살아있는 줄기세포의 정보를 저장할 큐를 생성
    Q = []
    for n in range(N):
        for m in range(M):
            # 살아있는 세포는 큐에 넣어서 관리(행좌표, 열좌표)
            # 세포 정보는 board에 저장 생명력 / 상태(비활성 : 1, 활성 : 2) / 생성 후 경과 시간
            # 생성 후 경과시간이 X가 되면 상태가 1 -> 2로 변경
            # 생성 후 경과시간이 X + 1이 되면 분열
            # 생성 후 경과시간이 2X가 되면 죽은것이니 큐에서 제거
            # 최종적으로 큐의 길이를 출력(살아있는 세포의 개수)
            X = init[n][m]
            if X:
                # 배양 용기의 중앙에 줄기세포의 초기정보를 저장한다.
                board[K + n][K + m] = [X, 1, 0]
                # 살아있는 세포의 좌표값을 큐에 저장한다.
                Q.append((K + n, K + m))
    # print(board)
    # print(Q)

    # 배양 시간만큼 반복한다.
    for k in range(K):
        pop_targets = []
        for i in range(len(Q)):
            cr, cc = Q[i]
            X, status, time = board[cr][cc][0], board[cr][cc][1], board[cr][cc][2]

            # 시간 경과
            time += 1
            board[cr][cc][2] = time

            # 비활성 -> 활성
            if time == X:
                status = 2
                board[cr][cc][1] = status

            # 분열
            if time == X + 1:
                cell_split(X, cr, cc)

            # 죽음
            if time == 2 * X:
                pop_targets.append(i)
                status = 3
                board[cr][cc][1] = status

        pop_targets.sort(reverse=True)
        for p in pop_targets:
            Q.pop(p)


    result = len(Q)
    print('#{} {}'.format(tc, result))