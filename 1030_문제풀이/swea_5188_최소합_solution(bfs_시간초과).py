import sys
from collections import deque
sys.stdin = open('swea_5188_최소합.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    N = 13
    cnt = 0
    Q = deque()
    Q.append([0, 0, arr[0][0]])
    visit = [[0] * N for _ in range(N)]
    while Q:
        x, y, dist = Q.popleft()
        visit[x][y] += 1
        if x == N - 1 and y == N - 1:
            cnt += 1
            # dist가 최소인경우 저장
        else:
            if x + 1 < N: # 아래
                Q.append([x + 1, y, dist + arr[x + 1][y]])
            if y + 1 < N: # 오른쪽
                Q.append([x, y + 1, dist + arr[x][y + 1]])
    print(cnt)
    for lst in visit:
        print(*lst)