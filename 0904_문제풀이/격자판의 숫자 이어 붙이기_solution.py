import sys
sys.stdin = open('격자판의 숫자 이어 붙이기.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, cnt, number):
    if cnt == 6: # 숫자 7개를 모두 만들었으면, 더 이상 재귀호출 X
        result.add(number)
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            new_number = number + board[nr][nc]
            dfs(nr, nc, cnt+1, new_number)

N = 4
T = int(input())
for tc in range(1, T+1):
    board = [input().split() for _ in range(N)]
    # 중복되지 않는 것만 저장한다.
    result = set()
    # 모든 칸은 시작점이 될 수 있다.
    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, board[i][j])


    print("#{} {}".format(tc, len(result)))