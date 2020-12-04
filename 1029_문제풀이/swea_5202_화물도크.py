import sys
sys.stdin = open('swea_5202_화물도크.txt')

def powerset(select, idx):
    global result

    if idx == N:
        # print(select)
        tmp = sum(select)
        if result < tmp:
            result = tmp
        return

    s, e = apl[idx]

    # 해당 화물차의 상하차가 가능한지 확인
    pos = True
    if sum(timetable[s:e]) != 0:
        pos = False

    # 해당 화물차의 상하차가 가능할때 선택한 경우
    if pos:
        select[idx] = 1
        for j in range(s, e):
            timetable[j] = 1
        powerset(select, idx + 1)
        # 재귀 호출이 끝나면 다시 그 시간을 사용할 수 있게 만든다.
        for j in range(s, e):
            timetable[j] = 0

    # 그 화물차를 선택하지 않은 경우
    select[idx] = 0
    powerset(select, idx + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    apl = []
    for i in range(N):
        apl.append(list(map(int, input().split())))
    # print(apl)

    # 작업 종료와 동시에 작업을 시작할 수 있으므로 작업종료 시간은 1로 채우지 않는다.
    # 작업 시작이 불가능한 시간만 1로 채운다.
    timetable = [0] * 25
    select = [0] * N
    result = 0

    powerset(select, 0)

    print('#{} {}'.format(tc, result))





