import sys
sys.stdin = open('swea_1247_최적경로.txt')


def perm(idx, dis, x, y):
    # idx 몇번째 방문 고객, dis 이동거리, x, y 현재 좌표
    global min_dis
    if dis >= min_dis:
        return
    if idx == N:
        # 집으로 돌아가는 것을 추가한다.
        to_home = abs(x - e[0]) + abs(y - e[1])
        case_dis = dis + to_home
        min_dis = min(min_dis, case_dis)
        return
    for i in range(N):
        if not route[i]:
            route[i] = 1
            tmp = abs(x - pos[i][0]) + abs(y - pos[i][1])
            perm(idx + 1, dis + tmp, pos[i][0], pos[i][1])
            route[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 고객의 수
    arr = list(map(int, input().split()))
    pos = []
    for i in range(N + 2):
        pos.append((arr[2*i], arr[2*i+1]))
    s = pos.pop(0)
    e = pos.pop(0)
    route = [0] * N
    # print(route)
    min_dis = 0xffffffff
    perm(0, 0, s[0], s[1])
    print('#{} {}'.format(tc, min_dis))

