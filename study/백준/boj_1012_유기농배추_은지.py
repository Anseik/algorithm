#유기농배추
import sys
sys.stdin = open('boj_1012_유기농배추_안세익.txt')

T = int(input())
for _ in range(1, T + 1):
    M, N, K = map(int, input().split())
    matrix = [[0] * (M + 2) for _ in range(N + 2)]

    for _ in range(K):
        a, b = map(int, input().split())
        matrix[b + 1][a + 1] = 1
    #print(*matrix)
    #---- 입력받기 종료

    dy = [-1, 0, 0, 1]
    dx = [0, 1, -1, 0]
    result = []

    def getResult(y,x): #(y,x)부터 시작해서 DFS하면서 인접한 배추의 갯수를 반환하는 함수
        cnt = 1
        matrix[y][x] = 0 #방문했으니 0으로

        for k in range(4):
            yy = y + dy[k]
            xx = x + dx[k]

            if matrix[yy][xx]:
                cnt += getResult(yy, xx)

        return cnt

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if matrix[j][i]:
                result.append(getResult(j, i))

    print(len(result))