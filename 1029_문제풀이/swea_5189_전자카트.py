import sys
sys.stdin = open('swea_5189_전자카트.txt')

def perm(idx):
    global result
    if idx == len(route):
        # 순열의 처음과 끝에 사무실을 추가한다.
        line = [0] + route + [0]
        # print(line)
        tmp = 0
        for j in range(len(line) - 1):
            s = line[j]
            e = line[j + 1]
            tmp += arr[s][e]
        if result > tmp:
            result = tmp

        return

    for i in range(idx, len(route)):
        route[idx], route[i] = route[i], route[idx]
        perm(idx + 1)
        route[idx], route[i] = route[i], route[idx]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N, arr)

    # 사무실은 제외하고 배열을 생성한다.
    route = [i for i in range(1, N)]
    result = 100 * N
    perm(0)

    print('#{} {}'.format(tc, result))
