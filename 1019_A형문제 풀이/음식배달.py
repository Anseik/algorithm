import sys
import copy
sys.stdin = open('음식배달.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(case, r, c):
    distance = 0
    Q = []
    Q.append((r, c, distance))
    while Q:
        cr, cc, distance = Q.pop(0)
        if case[cr][cc] >= 2:
            return distance
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 < nr < N and 0 < nc < N:
                Q.append((nr, nc, distance + 1))


def comb(select, idx ,cnt):
    global result
    if idx == len(select):
        # 한개 이상의 가게가 선택되어야 한다.
        if cnt != 0:
            # 선택된 가게의 좌표값
            choice = []
            # 선택된 가게의 운영비
            cost = 0
            for i in range(len(select)):
                if select[i] == 1:
                    choice.append(stores[i])
                    cost += arr[stores[i][0]][stores[i][1]]
            # 백트래킹 1
            if cost >= result:
                return
            # print(choice)

            # 선택되지 않은 가게는 0으로 변경하고 집에서 가장가까운 가게까지 bfs를 실행해서 최소값을 비교한다.
            # 원본 배열은 수정하지 않기위해 깊은 복사 이용
            case = copy.deepcopy(arr)

            for j in range(len(stores)):
                if stores[j] not in choice:
                    case[stores[j][0]][stores[j][1]] = 0
            # print(case)

            # case를 돌며 운영비에 집에서 가장 가까운 가게까지의 거리를 더한다.
            case_result = cost
            for r in range(N):
                for c in range(N):
                    # 집에서 최단거리 가게까지의 거리
                    if case[r][c] == 1:
                        distance = bfs(case, r, c)
                        case_result += distance

                    # 백트래킹 2
                    if case_result >= result:
                        return

            if case_result < result:
                result = case_result
        return

    # idx번째 가게가 선택된 경우
    select[idx] = 1
    comb(select, idx + 1, cnt + 1)
    # idx번째 가게가 선택되지 않은 경우
    select[idx] = 0
    comb(select, idx + 1, cnt)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(arr)

    stores = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] >= 2:
                stores.append((r, c))
    # print(stores)


    select = [0] * len(stores)
    result = float('inf')
    comb(select, 0, 0)
    print("#{} {}".format(tc, result))

