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

    # 순회는 도착점 부터 역순으로 시작
    r = 99
    c = end

    # 방문여부 확인
    visited = [[0] * N for _ in range(N)]

    def dfs(r, c):
        visited[r][c] = 1

        if r == 0: # 시작점에 도착했으면 시작점의 열의 좌표(c)를 반환
            return c

        if c > 0:
            if data[r][c - 1] == 1 and visited[r][c - 1] != 1:  # 좌측 뱡향으로 길이 있고 방문한적이 없으면
                c -= 1
                return dfs(r, c)

        if c < 99:
            if data[r][c + 1] == 1 and visited[r][c + 1] != 1:  # 우측 뱡향으로 길이 있고 방문한적이 없으면
                c += 1
                return dfs(r, c)

        # 좌우측 둘다 길이 없으면 위로 이동(여기까지 올때까지 return을 만나지 못했으면)
        r -= 1
        return dfs(r, c)

    result = dfs(r, c)

    print("#{} {}".format(tc, result))
