import sys
sys.stdin = open('동철이의 일 분배.txt')


def dfs(r, case_per):
    global max_per

    if case_per < max_per:
        return

    if r == N:
        if case_per > max_per:
            max_per = case_per
        return

    for c in range(N):
        if not work[c]:
            if per[r][c] == 0:
                continue
            work[c] = 1
            dfs(r + 1, case_per * per[r][c])
            work[c] = 0
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    per = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            per[i][j] = per[i][j] / 100

    # 주어진 일이 모두 성공할 확률의 최대값
    max_per = 0

    # 일의 담당이 정해졌는지 체크하기 위한 배열
    work = [0] * N

    dfs(0, 1)
    result = format(max_per * 100, ".6f")
    print("#{} {}".format(tc, result))