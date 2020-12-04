import sys
sys.stdin = open('SWEA_보급로.txt')

def bfs(): #(0,0)에서 시작해서 (n-1, n-1)까지 순회할 때 최소복구시간을 찾는 함수
    # 좌, 우, 상, 하
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    cost[0][0] = 0 #시작지점의 복구시간 기록

    queue = []
    queue.append((0, 0))
    while queue:
        r, c = queue.pop(0)

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # if문에 매번 0 <= nr < N and 0 <= nc < N 이거 적기 싫어서 컨티뉴로 거름
            if 0 > nr or nr >= N or 0 > nc or nc >= N:
                continue

            if cost[r][c] + matrix[nr][nc] < cost[nr][nc]:
                queue.append((nr, nc))
                cost[nr][nc] = cost[r][c] + matrix[nr][nc]

    return


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        matrix = [list(map(int, input())) for _ in range(N)] # 지도
        cost = [[float('inf')] * N for _ in range(N)] # cost에 최댓값으로 다 넣기(최단 복구시간 저장 배열)
        bfs()
        print(f'#{tc} {cost[N-1][N-1]}')