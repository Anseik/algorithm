import sys
sys.stdin = open('음식배달.txt')

def comb(select, idx ,cnt):
    global result
    if idx == len(select):
        # 한개 이상의 가게가 선택되어야 한다.
        if cnt != 0:
            case_result = 0
            # 집에서 가장 가까운 가게까지의 거리
            for h in range(len(homes)):
                hdis = float('inf')
                for s in range(len(stores)):
                    if select[s] == 1:
                        hdis = min(hdis, dis[s][h])
                case_result += hdis

            # 선택된 가게의 운영비
            for s in range(len(stores)):
                if select[s] == 1:
                    case_result += stores[s][2]

            if result > case_result:
                result = case_result

        return # 1개의 가게도 선택되지 않은 경우는 없다.

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

    homes, stores = [], []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                homes.append((r, c))
            if arr[r][c] >= 2:
                cost = arr[r][c]
                stores.append((r, c, cost))
    # print(homes)
    # print(stores)

    # 집과 가게 간의 거리를 전처리 한다.
    dis = [[0] * len(homes) for _ in range(len(stores))]
    # print(dis)
    for s in range(len(stores)):
        for h in range(len(homes)):
            dis[s][h] = abs(homes[h][0] - stores[s][0]) + abs(homes[h][1] - stores[s][1])
    # print(dis)

    select = [0] * len(stores)
    result = float('inf')
    comb(select, 0, 0)
    print("#{} {}".format(tc, result))

