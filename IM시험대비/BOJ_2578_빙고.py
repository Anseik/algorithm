import sys
sys.stdin = open('BOJ_2578_빙고.txt')


def check_bingo():
    cnt = 0 # 사회자가 부른 횟수
    for host in hosts:
        cnt += 1
        for r in range(N):
            for c in range(N):
                if cs[r][c] == host:
                    check[r][c] = 1
                    bingo = 0
                    # 가로빙고 확인
                    for i in range(N):
                        row_cnt = 0
                        for j in range(N):
                            if check[i][j] == 1:
                                row_cnt += 1
                        if row_cnt == N:
                            bingo += 1

                    # 세로빙고 확인
                    for i in range(N):
                        col_cnt = 0
                        for j in range(N):
                            if check[j][i] == 1:
                                col_cnt += 1
                        if col_cnt == N:
                            bingo += 1

                    # 좌대각선 빙고 확인
                    left_cross_cnt = 0
                    for i in range(N):
                        for j in range(N):
                            if i == j and check[i][j] == 1:
                                left_cross_cnt += 1
                    if left_cross_cnt == N:
                        bingo += 1

                    # 우대각선 빙고 확인
                    right_cross_cnt = 0
                    for i in range(N):
                        for j in range(N):
                            if i + j == (N - 1) and check[i][j] == 1:
                                right_cross_cnt += 1
                    if right_cross_cnt == N:
                        bingo += 1

                    # 빙고가 됐는지 확인(3개 이상이면 빙고)
                    if bingo >= 3:
                        return cnt

T = 1
N = 5
for tc in range(1, T + 1):
    cs = [list(map(int, input().split())) for _ in range(N)]
    hosts = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in tmp:
            hosts.append(j)
    # print(cs)
    # print(hosts)
    check = [[0] * N for _ in range(N)]
    # print(check)

    result = check_bingo()
    print(result)

