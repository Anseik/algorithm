import sys
sys.stdin = open('Algo2_구미_1반_안세익.txt')

dr = [-1, 1, 0 ,0]
dc = [0, 0, -1, 1]
def dfs(r, c):
    global cnt
    # 터진 폭탄의 개수 카운트
    cnt += 1
    # 폭발력이 미치는 범위
    area = bombs[r][c]
    # 폭탄이 터지면 0으로 변경
    bombs[r][c] = 0
    for d in range(4):
        # 폭발력 만큼 폭탄이 터지도록 델타에 배수를 곱한다.
        for i in range(1, area + 1):
            nr = r + (dr[d] * i)
            nc = c + (dc[d] * i)
            if 0 <= nr < N and 0 <= nc < N and bombs[nr][nc]:
                dfs(nr, nc)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    R, C = map(int, input().split())
    bombs = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(R, C)
    # print(bombs)

    cnt = 0
    dfs(R, C)

    print("#{} {}".format(tc, cnt))