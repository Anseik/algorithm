# 현재 노드(위치)에서 갈수 있는 노드들을
# stack push 해서 다음노드로 넘어가거나
# dfs()재귀 콜해서 다음 단계로 넘어가기

import sys
sys.stdin = open('Ladder1.txt')

T = 10
N = 100
for t in range(T):
    tc = int(input())
    # data = [list(map(int, input().split())) for _ in range(N)]
    # # print(tc)
    # # print(data)
    # end = 0 # 2가 있는 열의 위치
    # for i in range(N):
    #     if data[99][i] == 2:
    #         end = i

    arr = [list(map(int,input().split())) for _ in range(N)]
    data = [[0] * 102 for _ in range(102)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            data[i+1][j+1] = arr[i][j]
            if data[i+1][j+1] == 2:
                end = j+1

    # 델타 활용
    # 좌 우
    dr = [0, 0]
    dc = [-1, 1]

    r = 99
    c = end
    d1 = 0
    d = d1 % 2

    # 방문여부 확인
    visited = [[0] * 102 for _ in range(102)]

    def dfs(r, c):
        global d1
        global d
        visited[r][c] = 1

        if r == 0: # 시작점까지 왔으면
            return c # 시작점의 열의 좌표를 반환한다.

        r = r + dr[d]
        c = c + dc[d]
        if data[r][c] == 1 and visited[r][c] != 1 and 1 <= r <= 100 and 1 <= c <= 100: # 델타 뱡향으로 길이 있고 방문한적이 없으면
            return dfs(r, c)

        r = r - dr[d]
        c = c - dc[d]


        d1 = d1 + 1
        d= d1 % 2
        r = r + dr[d]
        c = c + dc[d]
        if data[r][c] == 1 and visited[r][c] != 1 and 1 <= r <= 100 and 1 <= c <= 100: # 반대 방향으로 길이 있고 방문한적이 없으면
            return dfs(r, c)

        else: # 양쪽 다 길이 없으면 원점으로 돌아와 위로 이동하고 델타를 초기화
            r = r - dr[d]
            c = c - dc[d]
            r = r - 1
            d1 = d1 - 1
            d = d1 % 2
            return dfs(r, c)


    result = dfs(r, c)

    print("#{} {}".format(tc, result -1))
