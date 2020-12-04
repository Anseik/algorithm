import sys
sys.stdin = open('추억의 2048게임.txt')

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
D = {
    'left': 0,
    'right': 1,
    'up': 2,
    'down': 3
}
T = int(input())
for tc in range(1, T + 1):
    n, s = input().split()
    n = int(n)
    b = [list(map(int, input().split())) for _ in range(n)]
    c = set()
    k = range(n) if s in 'upleft' else range(n-1, -1, -1)
    for i in k:
        for j in k:
            if b[i][j]: # 값이 있을 때
                cr, cc = i, j
                nr, nc = cr + dr[D[s]], cc + dc[D[s]]
                while 0 <= nr < n and 0 <= nc < n:
                    if b[nr][nc] == 0: # 비어있으면 swap
                        b[cr][cc], b[nr][nc] = b[nr][nc], b[cr][cc]
                    elif b[cr][cc] == b[nr][nc] and (nr, nc) not in c: # 숫자가 같고 새로만들어 진 타일이 아니면
                        c.add((nr, nc))
                        b[nr][nc] *= 2 # 합치고
                        b[cr][cc] = 0 #
                        break
                    else: # 숫자가 다른 다른 타일이 있을때
                        break
                    cr, cc = nr, nc
                    nr += dr[D[s]]
                    nc += dc[D[s]]

    print('#{}'.format(tc))
    for i in b:
        print(*i)