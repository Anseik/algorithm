import sys
sys.stdin = open('추억의 2048게임.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# S에 따른 델타 인덱스
D = {
    'up': 0,
    'down': 1,
    'left': 2,
    'right': 3
}

T = int(input())
for tc in range(1, T + 1):
    N, S = input().split()
    N = int(N)
    B = [list(map(int, input().split())) for _ in range(N)]

    NT = [[0] * N for _ in range(N)] # 새로 만들어진 타일의 위치를 저장

    d = D[S] # 델타는 S에 따라 고정

    # 벽에 가까운 쪽부터 먼저 민다고 생각해야 하므로
    # up, left일때는 0 ~ (N - 1), down, right일때는 (N - 1) ~ 0 순으로 반복문을 돌아야 한다.
    K = range(N) if S == 'up' or S == 'left' else range(N - 1, -1, -1)

    for r in K:
        for c in K:
            if B[r][c]: # 0이 아닐때
                cr, cc = r, c
                nr = cr + dr[d]
                nc = cc + dc[d]
                while 0 <= nr < N and 0 <= nc < N:

                    if not B[nr][nc]: # 다음 칸이 비어있으면
                        B[nr][nc] = B[cr][cc]
                        B[cr][cc] = 0

                    elif B[nr][nc] == B[cr][cc] and not NT[nr][nc]: # 다음 칸이 같은 숫자의 타일이고 그 타일이 새로 만들어진 타일이 아니면
                        B[nr][nc] *= 2 # 합친다.
                        B[cr][cc] = 0 # 옮기던 타일은 없앤다.
                        NT[nr][nc] = 1 # 새로 만들어진 타일의 위치를 저장한다.
                        break # 옮기던 타일이 없어졌으므로 더 이상 진행하지 않는다.

                    else: # 다른 타일이 있는데 숫자가 다르면 더 이상 진행할 수 없다.
                        break

                    cr, cc = nr, nc # 인덱스를 델타 방향으로 한 칸 이동시키고 계속 진행
                    nr = cr + dr[d]
                    nc = cc + dc[d]

    print("#{}".format(tc))
    for row in B:
        print(*row)
