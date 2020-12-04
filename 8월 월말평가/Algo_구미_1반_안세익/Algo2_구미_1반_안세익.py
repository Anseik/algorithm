import sys
sys.stdin = open('Algo2_구미_1반_안세익.txt')

def dfs(r, c):
    arr[r][c] = 0 # 지나간 곳은 0으로 변경
    # 델타 : 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 사방으로 탐색 시작
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1: #범위체크 및 연못인지 체크
            dfs(nr, nc) # 연결된 연못 위치에서 dfs 함수 재귀 호출

T = int(input())
for tc in range(1, T+1):
    # M : 마당의 가로 길이
    # N : 마당의 세로 길이
    # K : 연못 좌표 개수
    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        # print(x, y)
        arr[y][x] = 1
    # print(arr)

    cnt = 0 # 물고기의 마리수를 카운트하는 변수
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1: # arr전체를 순회하다가 연못이면 dfs실행
                cnt += 1 # 물고기 한마리 추가
                dfs(r, c) # dfs 실행결과 확인한 연못 위치가 0으로 변경된다.

    print("#{} {}".format(tc, cnt))
