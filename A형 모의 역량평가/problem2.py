import sys
sys.stdin = open('problem2.txt')

T = int(input())
for tc in range(1, T + 1):
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    # print(W, H)
    # print(arr)

    # 집의 위치 저장
    homes = []
    hr = set()
    hc = set()
    for r in range(H):
        for c in range(W):
            if arr[r][c] == 1:
                homes.append((r, c))
                hr.add(r)
                hc.add(c)
    # print(homes)
    # print(hr)
    # print(hc)


    min_dist = 987654321
    # 행순회, 열순회, 대각선 순회를하며 도로를 건설할 수 있는 위치를 찾아 낸다.

    # 행순회
    for i in range(H):
        if i not in hr:
            for j in range(W):
                if arr[i][j] == 1:
                    break

            else:
                # 도로를 건설할 수 있는 경우 도로의 위치를 저장
                roads = []
                for j in range(W):
                    roads.append((i, j))
                # print(roads)

                # 집에서 도로의 격자점까지 최소거리를 구하고 그 중에 가장 멀리 떨어져 있는 것(max(dist))을 저장한다.
                dist = []
                for home in homes:
                    tmp = 987654321
                    for road in roads:
                        if tmp > abs(home[0] - road[0]) + abs(home[1] - road[1]):
                            tmp = abs(home[0] - road[0]) + abs(home[1] - road[1])
                    dist.append(tmp)
                # print(dist)
                min_dist = min(min_dist, max(dist))

    # 열순회
    for j in range(W):
        if j not in hc:
            for i in range(H):
                if arr[i][j] == 1:
                    break

            else:
                # 도로를 건설할 수 있는 경우 도로의 위치를 저장
                roads = []
                for i in range(H):
                    roads.append((i, j))
                # print(roads)

                # 집에서 도로의 격자점까지 최소거리를 구하고 그 중에 가장 멀리 떨어져 있는 것(max(dist))을 저장한다.
                dist = []
                for home in homes:
                    tmp = 987654321
                    for road in roads:
                        if tmp > abs(home[0] - road[0]) + abs(home[1] - road[1]):
                            tmp = abs(home[0] - road[0]) + abs(home[1] - road[1])
                    dist.append(tmp)
                # print(dist)
                min_dist = min(min_dist, max(dist))

    # 대각선 순회(좌하 우상)
    start = []
    for i in range(1, H):
        start.append((i, 0))
    for k in range(1, W - 1):
        start.append((H - 1, k))
    # print(start)
    for j in range(len(start)):
        roads = []
        r, c = start[j]
        if (r, c) in homes:
            continue
        else:
            roads.append((r, c))
            pos = True
            while not (r == 0 or c == W - 1):
                r -= 1
                c += 1
                if (r, c) in homes:
                    pos = False
                    break
                else:
                    roads.append((r, c))

            if pos:
                dist = []
                for home in homes:
                    tmp = 987654321
                    for road in roads:
                        if tmp > abs(home[0] - road[0]) + abs(home[1] - road[1]):
                            tmp = abs(home[0] - road[0]) + abs(home[1] - road[1])
                    dist.append(tmp)
                # print(dist)
                min_dist = min(min_dist, max(dist))



    # 대각선 순회(좌상 우하)
    start = []
    for i in range(1, H):
        start.append((i, W - 1))
    for k in range(1, W - 1):
        start.append((H - 1, k))
    # print(start)
    for j in range(len(start)):
        roads = []
        r, c = start[j]
        if (r, c) in homes:
            continue
        else:
            roads.append((r, c))
            pos = True
            while not (r == 0 or c == 0):
                r -= 1
                c -= 1
                if (r, c) in homes:
                    pos = False
                    break
                else:
                    roads.append((r, c))

            if pos:
                dist = []
                for home in homes:
                    tmp = 987654321
                    for road in roads:
                        if tmp > abs(home[0] - road[0]) + abs(home[1] - road[1]):
                            tmp = abs(home[0] - road[0]) + abs(home[1] - road[1])
                    dist.append(tmp)
                # print(dist)
                min_dist = min(min_dist, max(dist))

    if min_dist == 987654321:
        min_dist = -1
    print('#{} {}'.format(tc, min_dist))

