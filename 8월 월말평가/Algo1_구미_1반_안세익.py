import sys
sys.stdin = open('Algo1_구미_1반_안세익.txt')

# 팔방 순회하며 값이 0인 곳을 규칙에 맞게 채워나가는 함수 / stack을 이용한 dfs
def dfs(r, c, m, d):
    m += d # m은 채워넣을 값, d는 변화량
    # 델타(상, 상우, 우, 하우, 하, 하좌, 좌, 상좌)
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    stack = list()
    stack.append((r, c))
    while stack:
        cr, cc = stack[0] # 가장 먼저들어간 요소를 가져온다.
        er, ec = 0, 0 # 동심원의 종점, 12시부터 값을 채워넣기 시작해 시계방향으로 채워넣고 11시 방향(좌측상단 모서리에 왔을때가 종점)
        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0: # 범위검사 및 값이 채워져 있지 않은지 확인 후
                arr[nr][nc] = m # 해당 자리에 값을 채워 넣는다.
                stack.append((nr, nc)) # stack에 해당 위치 좌표를 저장한다.
                er, ec = nr, nc  # nr, nc를 각각 er, ec에 저장한다. for문이 끝나고 나면 종점에 있는지 확인하는 용도로 사용한다.
        stack.pop(0) # for문 밖으로 나오면 더 이상 그 위치와 인접한 좌표 중 값을 채워넣을 수 있는 것이 없으므로 pop한다.
        if er == ec: # 동심원이 12시에서 시작하여 시계방향으로 한 바퀴를 돌아 마지막 지점(좌측상단 모서리에 도착하면) 다음 동심원으로 넘어가므로 변화량을 증가 시킨다.
            m += d


T = int(input())
for tc in range(1, T+1):
    # N : 배열의 크기
    # M : 첫 번째 입력 값
    # D : 변경 값
    N, M, D = map(int, input().split())
    # print(tc)
    # print(N, M, D)

    arr = [[0] * N for _ in range(N)] # 배열 초기화
    # print(arr)

    s = N // 2 # 중앙점(시작점)
    arr[s][s] = M # 중앙점에 값을 먼저 채워 넣는다.

    # 팔방 순회하며 조건에 맞는 곳에 값을 채워 나가기
    # dfs함수 실행
    dfs(s, s, M, D)

    print("#{}".format(tc), end=" ")
    for row in arr:
        print(sum(row), end=" ")
    print()
