import sys
sys.stdin = open('잔디깎기.txt')

# 만들 수 있는 모양의 조건
# 모든 칸에서 시작해 정원 밖으로 나갈 수 있어야 한다.
# 단, 이동은 다음 칸이 시작점에 적힌 값보다 작거나 같을때만 할 수 있다.

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check(r, c):
    visit[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M: # 정원 밖으로 나가면
            return 1
        elif garden[nr][nc] <= tmp and not visit[nr][nc]: # 이동할 수 있으면
            return check(nr, nc)

    return 0 # 더 이상 이동 못하면 그 모양을 만들 수 없다.


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    garden = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M)
    # print(garden)

    ans = 0
    for r in range(N):
        for c in range(M):
            tmp = garden[r][c]
            visit = [[0] * M for _ in range(N)]
            ans = check(r, c)
            if ans == 1:
                continue
            else:
                break
        if ans == 0:
            break

    print("#{}".format(tc), end = " ")
    if ans:
        print('YES')
    else:
        print('NO')