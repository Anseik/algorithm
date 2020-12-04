# 현재 노드(위치)에서 갈수 있는 노드들을
# stack push 해서 다음노드로 넘어가거나
# dfs()재귀 콜해서 다음 단계로 넘어가기

import sys
sys.stdin = open('Ladder1.txt')

T = 10
N = 100
for t in range(T):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    end = 0 # 2가 있는 열의 위치(도착점의 열의 좌표)
    for i in range(N):
        if data[99][i] == 2:
            end = i

    # 델타 활용(좌, 우)
    dr = [0, 0]
    dc = [-1, 1]

    # 순회는 도착점 부터 역순으로 시작
    r = 99
    c = end
    d = 0 # 가로방향 탐색 간 같은 방향에 길이 계속 있는 경우 델타를 유지하기 위해 전역변수로 선언

    # 방문여부 확인
    visited = [[0] * N for _ in range(N)]

    def dfs(r, c):
        global d
        visited[r][c] = 1

        if r == 0: # 시작점까지 왔으면
            return c # 시작점의 열의 좌표를 반환한다.

        r += dr[d]
        c += dc[d]
        if 0 <= r <= 99 and 0 <= c <= 99:
            if data[r][c] == 1 and visited[r][c] != 1: # 델타 뱡향으로 길이 있고 방문한적이 없으면
                return dfs(r, c)

        r -= dr[d]
        c -= dc[d]
        d = (d + 1) % 2
        r += dr[d]
        c += dc[d]
        if 0 <= r <= 99 and 0 <= c <= 99:
            if data[r][c] == 1 and visited[r][c] != 1: # 반대 방향으로 길이 있고 방문한적이 없으면
                return dfs(r, c)

        # 양쪽 다 길이 없으면 원점으로 돌아와 위로 이동하고 델타를 초기화
        r -= dr[d]
        c -= dc[d]
        r -= 1
        d = 0
        return dfs(r, c)


    result = dfs(r, c)

    print("#{} {}".format(tc, result))
