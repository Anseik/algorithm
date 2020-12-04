import sys
sys.stdin = open('BOJ_2564_경비원.txt')


T = 1
for tc in range(1, T + 1):
C, R = map(int, input().split())
N = int(input())
area = [[-2] * (C + 1) for _ in range(R + 1)]

# 길인 곳을 -1으로 초기화
for r in range(R + 1):
    for c in range(C + 1):
        if r == 0 or c == 0 or r == R or c == C:
            area[r][c] = -1

# 1북, 2남, 3서, 4동
store = []
sr, sc = 0, 0
st_num = 0
for i in range(N + 1):
    st_num += 1
    direction, length = map(int, input().split())
    r, c = 0, 0
    if direction == 1:
        c = length
    elif direction == 2:
        r = R
        c = length
    elif direction == 3:
        r = length
    elif direction == 4:
        r = length
        c = C
    if i == N:
        area[r][c] = 0
        sr, sc = r, c
    else:
        area[r][c] = st_num
        store.append((r, c))

# print(area)
# print(store)
# print(sr, sc)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = 0
st_num = 1
for i in range(N):
    Q = [(sr, sc, 0)]
    distance = 0
    while Q:
        cr, cc, cnt = Q.pop(0)
        if area[cr][cc] == st_num:
            distance = cnt
            break
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr <= R and 0 <= nc <= C and area[nr][nc] != -2:
                Q.append((nr, nc, cnt + 1))


    result += distance
    st_num += 1

print(result)







