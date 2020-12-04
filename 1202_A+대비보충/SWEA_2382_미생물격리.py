import sys
sys.stdin = open('SWEA_2382_미생물격리.txt')

# 이동 함수
def move(group):
    # 상
    if group[3] == 1:
        group[0] -= 1
    # 하
    elif group[3] == 2:
        group[0] += 1
    # 좌
    elif group[3] == 3:
        group[1] -= 1
    # 우
    elif group[3] == 4:
        group[1] += 1

    # 가장자리에 도착해 약품에 닿게 되는 경우
    if not (1 <= group[0] < N - 1 and 1 <= group[1] < N - 1):
        group = boundary(group)

    return group


# 미생물 수 감소 / 이동방향 변경 함수
def boundary(group):
    # 미생물 수 감소
    group[2] = group[2] // 2
    # 이동 방향을 반대방향으로 변경
    if   group[3] == 1: group[3] = 2
    elif group[3] == 2: group[3] = 1
    elif group[3] == 3: group[3] = 4
    elif group[3] == 4: group[3] = 3

    return group


# 같은 곳에 위치한 군집들을 합치는 함수
def combine_groups(groups):
    # 합쳐지는 경우 => cnt가 합쳐지고, dir은 cnt가 가장 큰 군집의 dir이 된다.
    new_groups = []
    for g in range(len(groups)):
        for n in range(len(new_groups)):
            if groups[g][0] == new_groups[n][0][0] and groups[g][1] == new_groups[n][0][1]:
                new_groups[n].append(groups[g])
                break
        else:
            new_groups.append([groups[g]])
    print(new_groups)

    groups = []
    for i in range(len(new_groups)):
        if len(new_groups[i]) == 1 and not new_groups[i][0][2] == 0:
            groups.append(new_groups[i][0])
        else:
            n_dir = 0
            max_cnt = 0
            sum_cnt = 0
            for j in range(len(new_groups[i])):
                sum_cnt += new_groups[i][j][2]
                if max_cnt < new_groups[i][j][2]:
                    max_cnt = new_groups[i][j][2]
                    n_dir = new_groups[i][j][3]
            groups.append([new_groups[i][0][0], new_groups[i][0][1], sum_cnt, n_dir])

    return groups


T = int(input())
for tc in range(1, T + 1):
    # N : 구역 크기, M : 격리 시간, K : 군집 개수
    N, M, K = map(int, input().split())
    groups = []
    for k in range(K):
        r, c, cnt, dir = map(int, input().split())
        groups.append([r, c, cnt, dir])
    # print(groups)

    # 격리 시간에 따른 변화
    for m in range(1, M + 1):
        # 현재 존재하는 군집의 다음 위치 계산 & 약품에 닿는지 확인
        for g in range(len(groups)):
            groups[g] = move(groups[g])

        # 군집 합치기
        groups = combine_groups(groups)

    result = 0
    for g in range(len(groups)):
        result += groups[g][2]
    print('#{} {}'.format(tc, result))


