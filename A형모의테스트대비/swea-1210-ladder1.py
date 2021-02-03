import sys
sys.stdin = open('swea-1210-ladder1.txt')

# 탐색 가능한 방향(좌, 우, 상)
dr = [0, 0, -1]
dc = [-1, 1, 0]

# 재귀를 이용한 dfs
def dfs_recursion(r, c):
    visit[r][c] = 1
    for d in range(3):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
            if nr == 0:
                return nc
            elif ladder[nr][nc] == 1:
                return dfs_recursion(nr, nc)

# 스택을 이용한 dfs
def dfs_stack(r, c):
    stack = list()
    stack.append((r, c))
    visit[r][c] = 1
    while stack:
        cr, cc = stack.pop()
        for d in range(3):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
                if nr == 0:
                    return nc
                elif ladder[nr][nc] == 1:
                    stack.append((nr, nc))
                    visit[nr][nc] = 1
                    break

T = 10
N = 100
for _ in range(T):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]
    # print(ladder)

    # 도착지점을 찾는다.
    er, ec = 99, 0
    for i in range(N):
        if ladder[er][i] == 2:
            ec = i
            break
    # print(ec)

    # 도착지점에서 역으로 dfs를 통해 올라가서 x값의 좌표(열좌표)를 찾는다.
    visit = [[0] * N for _ in range(N)]
    result = dfs_recursion(er, ec)
    print('#{} {}'.format(tc, result))