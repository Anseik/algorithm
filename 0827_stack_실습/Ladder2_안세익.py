import sys
sys.stdin = open('Ladder2_안세익.txt')

def dfs(r, c):
    visited[r][c] = 1
    global cnt
    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr <= 99 and 0 <= nc <= 99 and data[nr][nc] == 1 and visited[nr][nc] == 0:
            cnt += 1
            return dfs(nr, nc)
    else:
        return cnt

T = 10
N = 100
for t in range(T):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 델타: 좌, 우, 하
    dr = [0, 0, 1]
    dc = [-1, 1, 0]

    result = 0  # 가장 이동거리가 짧은 시작점의 열 좌표
    min_distance = N * N   # 가장 짧은 이동거리, 초기값은 나올 수 있는 가장 긴 이동거리인 N * N으로 설정
    for i in range(N):
        if data[0][i] == 1: # 출발 가능한 지점에 오면
            # 이동 시작
            r = 0
            c = i
            cnt = 0
            visited = [[0] * N for _ in range(N)]

            distance = dfs(r, c)
            if distance < min_distance:
                min_distance = distance
                result = i

    print("#{} {}".format(tc, result))
