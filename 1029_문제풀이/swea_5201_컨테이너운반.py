import sys
sys.stdin = open('swea_5201_컨테이너운반.txt')


T = int(input())
for tc in range(1, T + 1):
    # N : 컨테이너 수 / M : 트럭 수
    N, M = map(int, input().split())
    # 화물 무게
    ws = list(map(int, input().split()))
    # 이동한 화물의 총 중량이 최대가 되어야 하므로 내림차순으로 정렬
    ws.sort(reverse=True)
    # 적재용량
    ts = list(map(int, input().split()))
    # print(ws, ts)

    # 화물을 적재한 트럭을 표시하기 위한 배열생성
    load = [0] * M
    result = 0
    while True:
        if ws: # 실을 화물이 남아있으면
            target = ws.pop(0)
        else: # 실을 화물이 없으면 break
            break

        if sum(load) == M: # 모든 트럭이 화물을 실었으면 break
            break

        pos = []
        for i in range(M):
            if ts[i] >= target and not load[i]:
                pos.append((i, ts[i]))

        if not pos: # target을 실을 수 있는 트럭이 없으면 넘어간다.
            continue

        pos = sorted(pos, key = lambda x : x[1]) # target을 실을 수 있는 트럭 중 적재량이 가장 작은것은 찾는다.
        load[pos[0][0]] = 1 # 짐을 싣는다.
        result += target

    print('#{} {}'.format(tc, result))






