import sys
sys.stdin = open('swea_1953_탈주범검거.txt')

# 현재 위치에서 움직일 수 있는 방향
dir = {
    1: [0, 1, 2, 3], 2: [0, 1], 3: [2, 3],
    4: [0, 3], 5: [1, 3], 6: [1, 2], 7: [0, 2]
}

# 움직이려는 방향에 어떤 모양의 통로가 있어야 움직일 수 있는지
possible = {
    0: [1, 2, 5, 6], 1: [1, 2, 4, 7], 2: [1, 3, 4, 5], 3: [1, 3, 6, 7]
}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    result = 1
    queue = list()
    queue.append((r, c, 1))
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1

    while queue:
        cr, cc, cl = queue.pop(0)
        if cl == L:
            break
        # 움직일 수 있는 위치가 정해져 있음, 현재 위치의 통로 모양에 따라서 결정
        for i in dir[arr[cr][cc]]:
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                # i : 이동하는 방향
                if arr[nr][nc] in possible[i]:
                    queue.append((nr, nc, cl + 1))
                    visited[nr][nc] = 1
                    result += 1

    return result


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = bfs(R, C)
    print('#{} {}'.format(tc, result))