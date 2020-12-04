import sys
sys.stdin = open('정사각형 방.txt')

def bfs(r, c):
    global max_length, room_number
    que = list()
    que.append((r, c))
    cnt = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 사방 검사를 했을때 현재 방보다 1작은 방이 사방 중에 있으면
    # 검사를 하지 않아도 된다.
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if room[nr][nc] == room[r][c] - 1:
                return

    while que:
        cr, cc = que.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if room[nr][nc] == room[cr][cc] + 1:
                    que.append((nr, nc))
                    cnt += 1
                    break

    if cnt > max_length:
        max_length = cnt
        room_number = room[r][c]

    elif cnt == max_length:
        if room[r][c] < room_number:
            room_number = room[r][c]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0
    room_number = N * N
    # 모든 지점을 시작점으로 고려한다.
    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print("#{} {} {}".format(tc, room_number, max_length))