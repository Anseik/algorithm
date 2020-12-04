import sys
sys.stdin = open('Ladder1.txt')


def dfs():
    global ladder
    # 갈 수 있는 방향 좌, 우, 아래
    dr = [0, 0, 1]
    dc = [-1, 1, 0]
    # ladder의 첫번째 줄을 반복하면서 시작시점을 찾기
    for i in range(N):
        if ladder[0][i] == 1:
            # dfs 실행
            visited = [[0] * N for _ in range(N)]
            stack = list()
            stack.append((0, i)) # 시작지점 스택에 넣기
            while stack:
                cr, cc = stack.pop() # 현재위치
                visited[cr][cc] = 1
                for d in range(3):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                        if ladder[nr][nc] == 1:
                            stack.append((nr, nc))
                            break
                        elif ladder[nr][nc] == 2:
                            return i

    return -1 # 도착점을 못찾으면 -1 출력

T = 10
N = 100
for tc in range(T):
    tc = int(input())
    # 사다리 모양입력받고
    ladder = [list(map(int, input().split())) for _ in range(N)]
    # print(ladder)
    # 사다리 첫번째 줄 순회하면서, 1인지점(시작지점)을 찾음
    # 시작지점을 찾으면 dfs를 실행해서 목적지(2)까지 도착하면
    # 해당 시작 지점을 출력

    result = dfs()
    print("#{} {}".format(tc, result))