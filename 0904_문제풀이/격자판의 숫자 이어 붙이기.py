import sys
sys.stdin = open('격자판의 숫자 이어 붙이기.txt')

# 동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(r, c, result):

    # 길이가 7이면 즉 여섯번 이동하면서 숫자를 차례로 이어 붙였으면 추가하고 리턴
    if len(result) == 7:
        numbers.add(result)
        return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, result + grating[nr][nc])

N = 4
T = int(input())
for tc in range(1, T+1):
    grating = [input().split() for _ in range(N)]
    # print(grating)

    # 7자리 숫자의 집합
    numbers = set()

    for r in range(N):
        for c in range(N):
            result = grating[r][c]
            dfs(r, c, result)

    print("#{} {}".format(tc, len(numbers)))