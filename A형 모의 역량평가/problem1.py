import sys
sys.stdin = open('problem1.txt')


def count_time(selected):
    global min_time # 최소 시간 기록
    state = [] # 선택한 탈출구, 소요 시간, 상태(이동중1, 탈출대기중2, 탈출3)
    for i in range(len(selected)):
        if selected[i] == 0:
            state.append([0, mt[0][i], 1])
        if selected[i] == 1:
            state.append([1, mt[1][i], 1])
    # print(state)

    # 시간의 흐름 기록
    time = 0

    # 사람들의 탈출여부를 기록
    escape = [0] * len(M)

    # 시간에 따른 두 비상구의 상태 기록(대기인원)
    e0 = []
    e1 = []

    while sum(escape) < len(M): # 모든 사람이 탈출할때까지 계속
        # 시간이 증가한다.
        time += 1
        # 비상구의 대기 인원이 줄어든다.
        if len(e0) > 0:
            e0.pop(0)
        if len(e1) > 0:
            e1.pop(0)
        # 각 사람의 상태가 변화한다.
        a0 = a1 = False
        for j in range(len(state)):
            # 아직 탈출하지 못했으면 소요시간 감소
            if not escape[j]:
                if state[j][1] > 0:
                    state[j][1] -= 1

                # 이동중이었고 소요시간이 0이되면 탈출구에 도착했으니 대기인원 확인
                if state[j][2] == 1 and state[j][1] == 0:
                    # 0번 탈출구 도착
                    if state[j][0] == 0:
                        state[j][1] += len(e0)
                        e0.append('w')
                        state[j][2] = 2
                    # 1번 탈출구 도착
                    elif state[j][0] == 1:
                        state[j][1] += len(e1)
                        e1.append('w')
                        state[j][2] = 2

                # 대기중에 소요시간이 0이 되면 탈출
                # 탈출은 한번에 한 사람만 해야 되는데 동시에 탈출하는 경우가 생기나?
                elif state[j][2] == 2 and state[j][1] == 0:
                    if state[j][0] == 0 and a0 == False:
                        state[j][2] = 3
                        escape[j] = 1
                        a0 = True
                    elif state[j][0] == 1 and a1 == False:
                        state[j][2] = 3
                        escape[j] = 1
                        a1 = True

    # 모두 탈출 했을 때의 시간 측정, 최소 시간이면 갱신
    if min_time > time:
        min_time = time


def comb(selected, idx):
    if idx == len(M):
        # print(selected)
        count_time(selected)
        return

    selected[idx] = 0
    comb(selected, idx + 1)
    selected[idx] = 1
    comb(selected, idx + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(arr)


    # 사람과 비상구의 위치 기록
    M = []
    E = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                M.append((r, c))
            elif arr[r][c] == 2:
                E.append((r, c))
    # print(M, E)

    # 사람으로부터 비상구까지의 이동시간 전처리
    mt = [[0] * len(M) for _ in range(len(E))]
    for i in range(len(E)):
        for j in range(len(M)):
            mt[i][j] = abs(M[j][0] - E[i][0]) + abs(M[j][1] - E[i][1])
    # print(mt)

    #결과 저장
    min_time = 987654321

    # 각 사람이 두 비상구(1번, 2번) 중 어느 비상구를 선택할지 결정한다.(조합)
    selected = [-1] * len(M)
    comb(selected, 0)

    # 최소시간


    print('#{} {}'.format(tc, min_time))


